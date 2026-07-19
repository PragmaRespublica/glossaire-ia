# 🪁 Kite Marseille — vent & décisions

Petit site autonome (HTML/CSS/JS, aucun build, aucun backend) qui affiche les
conditions de vent sur les spots de kite autour de Marseille et donne un
verdict par spot : **vert / orange / rouge**, avec la raison et une taille
d'aile conseillée.

## Les 3 écrans

1. **Tableau** — vent moyen, rafales, direction, tendance sur les prochaines
   heures et verdict pour chaque spot.
2. **Reco** — une carte par spot avec photo/logo, verdict expliqué, taille
   d'aile conseillée selon votre poids, et notes sur le spot. Les réglages
   (poids, plage de vent navigable) se font en haut de cet écran et sont
   mémorisés dans le navigateur.
3. **Carte** — carte OpenStreetMap avec une pastille par spot : couleur du
   verdict, vitesse en nœuds et flèche de direction du vent.

## Lancer le site

C'est un site statique : ouvrez simplement `index.html` dans un navigateur,
ou servez le dossier :

```bash
cd kite
python3 -m http.server 8080
# puis http://localhost:8080
```

Déployable tel quel sur GitHub Pages, Netlify, Vercel…

## Ajouter vos images

Déposez vos photos/logos dans `assets/` avec ces noms (voir
`assets/README.md`) :

- `le-jai.jpg`, `carro.jpg`, `pointe-rouge.jpg`, `plage-napoleon.jpg`,
  `la-ciotat.jpg`

Tant qu'une image manque, un visuel de remplacement avec le nom du spot
s'affiche à la place.

## Configurer les spots

Tout se passe dans `js/config.js` :

- ajout/suppression de spots (nom, coordonnées, notes, image) ;
- **secteurs de vent favorables** par spot (`secteursIdeaux`,
  `secteursCorrects`) — à affiner selon votre connaissance du terrain, c'est
  ce qui pilote le verdict vert/orange/rouge ;
- plage de vent par défaut, seuil de rafales, fréquence d'actualisation.

## Source des données

[Open-Meteo](https://open-meteo.com/) : gratuit, sans clé d'API, interrogeable
directement depuis le navigateur. Ce sont des données de **modèle météo**
(mailles ~1–2 km, actualisées toutes les heures), pas des anémomètres
physiques posés sur les spots — fiable pour la tendance et le Mistral, moins
pour les effets très locaux (thermiques, déventes sous le relief).

Pour brancher un anémomètre réel plus tard : le réseau ouvert
[OpenWindMap/Pioupiou](https://www.openwindmap.org) expose une API publique
(`https://api.pioupiou.fr/v1/live/{id}`) — au moment de la création du site,
aucune balise active n'existait sur ces spots (celle de Marseille avait un
abonnement expiré). L'API des balises FFVL nécessite une clé
(informatique@ffvl.fr).

## Avertissement

Outil d'aide à la décision, pas un bulletin officiel : vérifiez toujours les
conditions sur place, la réglementation locale (zones et horaires de pratique,
notamment en été) et naviguez accompagné.
