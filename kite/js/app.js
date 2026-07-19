// ============================================================
// Kite Marseille — récupération du vent (Open-Meteo), calcul
// des verdicts par spot et rendu des trois écrans.
// ============================================================

const CARDINALES = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                    "S", "SSO", "SO", "OSO", "O", "ONO", "NO", "NNO"];

let reglages = chargerReglages();
let mesures = [];         // dernières données par spot (même ordre que SPOTS)
let map = null;
let calquesCarte = [];

// ---------- utilitaires ----------

function chargerReglages() {
  try {
    return { ...REGLAGES_DEFAUT, ...JSON.parse(localStorage.getItem("kite-reglages") || "{}") };
  } catch {
    return { ...REGLAGES_DEFAUT };
  }
}

function sauverReglages() {
  localStorage.setItem("kite-reglages", JSON.stringify(reglages));
}

function cardinale(deg) {
  return CARDINALES[Math.round(deg / 22.5) % 16];
}

function dansSecteur(deg, [debut, fin]) {
  deg = ((deg % 360) + 360) % 360;
  return debut <= fin ? deg >= debut && deg <= fin
                      : deg >= debut || deg <= fin;
}

function dansSecteurs(deg, secteurs) {
  return (secteurs || []).some((s) => dansSecteur(deg, s));
}

// ---------- verdict ----------

// Retourne { niveau: "vert"|"orange"|"rouge", label, raison }
function calculerVerdict(spot, m) {
  const { ventMin, ventMax } = reglages;
  const vent = m.vent, dir = m.direction;

  // 1. Direction : la sécurité d'abord, même si la force est bonne.
  let dirOk;
  if (dansSecteurs(dir, spot.secteursIdeaux)) dirOk = "ideale";
  else if (dansSecteurs(dir, spot.secteursCorrects)) dirOk = "correcte";
  else dirOk = "mauvaise";

  if (vent < ventMin - 3) return { niveau: "rouge", label: "Pas de vent", raison: `${vent} nds, trop léger pour naviguer` };
  if (dirOk === "mauvaise" && vent >= ventMin - 3)
    return { niveau: "rouge", label: "Mauvaise direction", raison: `Vent de ${cardinale(dir)} : offshore ou impraticable sur ce spot` };

  // 2. Force.
  let niveau, label, raison;
  if (vent < ventMin) {
    niveau = "orange"; label = "Léger";
    raison = `${vent} nds, tout juste — grande aile ou foil`;
  } else if (vent > ventMax + 5) {
    niveau = "rouge"; label = "Trop fort";
    raison = `${vent} nds, au-delà de votre plage`;
  } else if (vent > ventMax) {
    niveau = "orange"; label = "Costaud";
    raison = `${vent} nds, réservé aux confirmés bien toilés petit`;
  } else {
    niveau = "vert"; label = "C'est bon !";
    raison = `${vent} nds de ${cardinale(dir)}, dans votre plage`;
  }

  // 3. Dégradations : direction moyenne ou vent haché.
  if (niveau === "vert" && dirOk === "correcte") {
    niveau = "orange"; label = "Navigable";
    raison = `${vent} nds mais direction ${cardinale(dir)} pas optimale ici`;
  }
  if (niveau === "vert" && m.rafales / Math.max(vent, 1) > SEUIL_RAFALES) {
    niveau = "orange"; label = "Rafaleux";
    raison = `${vent} nds mais rafales à ${m.rafales} nds, vent irrégulier`;
  }
  return { niveau, label, raison };
}

// Surface d'aile conseillée (m²) — formule de pouce classique.
function tailleAile(vent) {
  if (vent < 8) return null;
  const t = Math.round((reglages.poids * 2.2) / vent);
  return Math.min(Math.max(t, 4), 17);
}

// Tendance : moyenne des 3 prochaines heures vs vent actuel.
function tendance(m) {
  if (!m.prochainesHeures.length) return { fleche: "→", texte: "stable" };
  const aVenir = m.prochainesHeures.slice(0, 3);
  const moy = aVenir.reduce((a, b) => a + b, 0) / aVenir.length;
  if (moy > m.vent + 2) return { fleche: "↗", texte: "en hausse" };
  if (moy < m.vent - 2) return { fleche: "↘", texte: "en baisse" };
  return { fleche: "→", texte: "stable" };
}

// ---------- données ----------

async function chargerVent() {
  const lats = SPOTS.map((s) => s.lat).join(",");
  const lons = SPOTS.map((s) => s.lon).join(",");
  const url = "https://api.open-meteo.com/v1/forecast" +
    `?latitude=${lats}&longitude=${lons}` +
    "&current=wind_speed_10m,wind_gusts_10m,wind_direction_10m" +
    "&hourly=wind_speed_10m&forecast_hours=4" +
    "&wind_speed_unit=kn&timezone=Europe%2FParis";

  const rep = await fetch(url);
  if (!rep.ok) throw new Error(`Open-Meteo ${rep.status}`);
  const donnees = await rep.json();
  const liste = Array.isArray(donnees) ? donnees : [donnees];

  mesures = liste.map((d) => ({
    vent: Math.round(d.current.wind_speed_10m),
    rafales: Math.round(d.current.wind_gusts_10m),
    direction: d.current.wind_direction_10m,
    heure: d.current.time,
    prochainesHeures: (d.hourly?.wind_speed_10m || []).slice(1),
  }));
}

// ---------- rendu ----------

function flecheDirection(deg) {
  // La flèche indique où va le vent (deg = d'où il vient).
  return `<span class="fleche-vent" style="transform: rotate(${(deg + 180) % 360}deg)">↑</span>`;
}

function badge(verdict) {
  return `<span class="badge badge-${verdict.niveau}">${verdict.label}</span>`;
}

function rendreTableau() {
  const tbody = document.querySelector("#table-spots tbody");
  tbody.innerHTML = SPOTS.map((spot, i) => {
    const m = mesures[i];
    if (!m) return `<tr><td>${spot.nom}</td><td colspan="5">—</td></tr>`;
    const v = calculerVerdict(spot, m);
    const t = tendance(m);
    return `<tr class="ligne-${v.niveau}">
      <td><strong>${spot.nom}</strong><br><small>${spot.commune}</small></td>
      <td>${badge(v)}</td>
      <td class="num">${m.vent} <small>nds</small></td>
      <td class="num">${m.rafales} <small>nds</small></td>
      <td>${flecheDirection(m.direction)} ${cardinale(m.direction)}</td>
      <td class="tendance" title="${t.texte}">${t.fleche}</td>
    </tr>`;
  }).join("");
}

function rendreReco() {
  document.getElementById("cartes-reco").innerHTML = SPOTS.map((spot, i) => {
    const m = mesures[i];
    if (!m) return "";
    const v = calculerVerdict(spot, m);
    const aile = tailleAile(m.vent);
    const t = tendance(m);
    return `<article class="carte-spot carte-${v.niveau}">
      <div class="carte-image">
        <img src="${spot.image}" alt="${spot.nom}" loading="lazy"
             onerror="this.replaceWith(Object.assign(document.createElement('div'),{className:'image-placeholder',textContent:'${spot.nom}'}))" />
      </div>
      <div class="carte-corps">
        <h2>${spot.nom} ${badge(v)}</h2>
        <p class="carte-mesures">${m.vent} nds (raf. ${m.rafales}) · ${cardinale(m.direction)} ${flecheDirection(m.direction)} · ${t.fleche} ${t.texte}</p>
        <p class="carte-raison">${v.raison}</p>
        ${aile && v.niveau !== "rouge" ? `<p class="carte-aile">Aile conseillée : <strong>~${aile} m²</strong> (pour ${reglages.poids} kg)</p>` : ""}
        <p class="carte-notes">${spot.notes}</p>
      </div>
    </article>`;
  }).join("");
}

const COULEURS = { vert: "#16a34a", orange: "#f59e0b", rouge: "#dc2626" };

function rendreCarte() {
  if (!map) {
    map = L.map("map", { zoomControl: true });
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 17,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
    map.fitBounds(SPOTS.map((s) => [s.lat, s.lon]), { padding: [40, 40] });
  }
  calquesCarte.forEach((c) => map.removeLayer(c));
  calquesCarte = [];

  SPOTS.forEach((spot, i) => {
    const m = mesures[i];
    if (!m) return;
    const v = calculerVerdict(spot, m);
    const icone = L.divIcon({
      className: "marqueur-spot",
      iconSize: [90, 80],
      iconAnchor: [45, 29],
      html: `<div class="pastille" style="border-color:${COULEURS[v.niveau]}">
               <span class="pastille-fleche" style="transform:rotate(${(m.direction + 180) % 360}deg)">↑</span>
               <span class="pastille-vent" style="color:${COULEURS[v.niveau]}">${m.vent}</span>
             </div>
             <div class="pastille-nom">${spot.nom}</div>`,
    });
    const marqueur = L.marker([spot.lat, spot.lon], { icon: icone }).addTo(map);
    marqueur.bindPopup(`<strong>${spot.nom}</strong> ${badge(v)}<br>
      ${m.vent} nds (raf. ${m.rafales}) · ${cardinale(m.direction)}<br>
      <small>${v.raison}</small>`);
    calquesCarte.push(marqueur);
  });
}

function rendreTout() {
  rendreTableau();
  rendreReco();
  if (map) rendreCarte();
  const heure = mesures[0]?.heure;
  document.getElementById("maj").textContent = heure
    ? `MàJ ${heure.slice(11, 16)}`
    : "";
}

// ---------- actualisation ----------

async function actualiser() {
  const majEl = document.getElementById("maj");
  try {
    await chargerVent();
    rendreTout();
  } catch (e) {
    console.error(e);
    majEl.textContent = "⚠ données indisponibles";
  }
}

// ---------- interactions ----------

document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((t) => t.classList.remove("actif"));
    document.querySelectorAll(".ecran").forEach((e) => e.classList.remove("actif"));
    tab.classList.add("actif");
    document.getElementById(tab.dataset.ecran).classList.add("actif");
    if (tab.dataset.ecran === "ecran-carte") {
      rendreCarte();
      setTimeout(() => map.invalidateSize(), 50);
    }
  });
});

document.getElementById("refresh").addEventListener("click", actualiser);

for (const [champ, cle] of [["poids", "poids"], ["vent-min", "ventMin"], ["vent-max", "ventMax"]]) {
  const input = document.getElementById(champ);
  input.value = reglages[cle];
  input.addEventListener("change", () => {
    const val = parseInt(input.value, 10);
    if (!Number.isNaN(val)) {
      reglages[cle] = val;
      sauverReglages();
      rendreTout();
    }
  });
}

// ---------- démarrage ----------

actualiser();
setInterval(actualiser, INTERVALLE_MAJ);
