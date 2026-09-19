---
name: gouv-fr-code-deploy
description: Préparer ou auditer le déploiement d'un service gouv-fr-code sur Cloud Pi Native, Kubernetes ou OpenShift. Utiliser pour adapter un conteneur ou un chart Helm aux contraintes rootless et de moindre privilège de la plateforme.
---

# Déployer sur Cloud Pi Native

## Références standard

- `role:platform-engineer` pour la stratégie de déploiement et d'exploitation.
- `skill:container-build` pour une image reproductible et rootless.
- `skill:kubernetes` et `skill:helm` pour les manifests, probes, ressources et
  validations usuelles.

## Spécificités Cloud Pi Native

- Appliquer le profil restreint : utilisateur non-root, racine en lecture seule,
  aucune élévation de privilèges et toutes les capacités Linux supprimées.
- Déclarer explicitement les volumes inscriptibles, notamment `/tmp`, avec une
  racine en lecture seule.
- Accepter l'UID dynamique attribué par OpenShift et écouter sur un port non
  privilégié.
- Injecter secrets et réglages d'environnement au déploiement, jamais dans
  l'image, le chart commun ou `values.yaml`.
- En plus des validations standard, tester le démarrage avec l'UID dynamique et
  l'absence de secret dans le rendu Helm.
