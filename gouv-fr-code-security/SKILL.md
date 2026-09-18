---
name: gouv-fr-code-security
description: Appliquer les garde-fous propres à l'environnement gouv-fr-code isolé par agent-vm. Utiliser lors d'un traitement de secrets ou données sensibles, d'un accès réseau, ou d'une opération Git distante depuis la VM.
---

# Travailler dans l'environnement sécurisé gouv-fr-code

## Règles non négociables

- Utiliser uniquement des données synthétiques dans les tests, fixtures, captures et prompts.
- Ne jamais écrire de clé, jeton, mot de passe ou donnée personnelle dans Git, les logs ou les sorties de l'agent.
- Conserver la vérification TLS et utiliser des requêtes SQL paramétrées.
- Ne pas contourner gitleaks avec `--no-verify`.
- N'ajouter une dépendance qu'après justification et examen de sa maintenance.

## Frontière agent-vm

- Ne pas monter les clés SSH, cookies ou répertoires personnels de l'hôte dans la VM.
- Utiliser un jeton dédié, révocable et de portée minimale lorsqu'un push ou une PR est nécessaire.
- Limiter les appels sortants aux domaines requis par la tâche.
- Expliquer toute élévation de privilèges ; éviter `sudo` et les chemins absolus propres à un utilisateur.
- Suspendre l'action et demander une validation humaine si la classification d'une donnée ou la portée d'un secret est incertaine.

## Avant livraison

1. Exécuter gitleaks sur l'historique et les fichiers suivis.
2. Rechercher les identifiants et données personnelles dans les fixtures et journaux.
3. Vérifier la portée et l'expiration des jetons utilisés.
4. Faire relire les changements qui touchent l'authentification, les autorisations ou les données sensibles.
