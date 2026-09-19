---
name: gouv-fr-code-security
description: Appliquer les garde-fous propres à l'environnement gouv-fr-code isolé par agent-vm. Utiliser lors d'un traitement de secrets ou données sensibles, d'un accès réseau, ou d'une opération Git distante depuis la VM.
---

# Travailler dans l'environnement sécurisé gouv-fr-code

## Références standard

- `role:security-reviewer` pour la revue des menaces, de l'authentification et des
  autorisations.
- `skill:secret-scanning` pour la détection de secrets dans les fichiers et
  l'historique Git.
- `skill:dependency-audit` pour l'examen des dépendances.

## Spécificités agent-vm

- Ne pas monter les clés SSH, cookies ou répertoires personnels de l'hôte dans la VM.
- Utiliser un jeton dédié, révocable et de portée minimale lorsqu'un push ou une PR est nécessaire.
- Limiter les appels sortants aux domaines requis par la tâche.
- Expliquer toute élévation de privilèges ; éviter `sudo` et les chemins absolus propres à un utilisateur.
- Suspendre l'action et demander une validation humaine si la classification d'une donnée ou la portée d'un secret est incertaine.
- Utiliser uniquement des données synthétiques dans les tests, captures et prompts.
- Ne jamais contourner le contrôle gitleaks avec `--no-verify`.
