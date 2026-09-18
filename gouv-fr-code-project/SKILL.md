---
name: gouv-fr-code-project
description: Configurer ou diagnostiquer un projet gouv-fr-code utilisant Albert, OpenCode et agent-vm. Utiliser pour le setup du projet, la sélection des MCP et skills, ou les variables AC_* de la VM.
---

# Configurer un projet gouv-fr-code

## Procédure

1. Exécuter `gouv-fr-code setup` une seule fois pour générer la configuration.
2. Conserver les règles propres au dépôt dans `AGENTS.md`.
3. Déclarer les skills chargés dans `.albert-code/skills.txt` ; ne sélectionner que ceux requis.
4. Configurer Albert dans `opencode.json` avec `AC_ALBERT_BASE_URL` plutôt qu'une URL dupliquée.
5. Activer les MCP à la demande : `data-gouv`, `context7`, `playwright` ou `chrome-devtools`.
6. Lancer la session isolée avec `gouv-fr-code run`.

## Conventions gérées

- Ne pas modifier hors besoin la zone délimitée par `gouv-fr-code:agents:start` et `gouv-fr-code:agents:end` dans `AGENTS.md`.
- Ne jamais écrire de jeton Albert dans `opencode.json` ou dans Git.
- Régler la VM avec `AC_VM_CPUS`, `AC_VM_MEMORY` et `AC_VM_DISK`.
- Utiliser `AGENT_VM_DIR` et `RUNTIME_VM_FILE` pour surcharger les emplacements, sans chemin utilisateur codé en dur.

## Vérification

- Vérifier que `opencode.json` est valide et que le provider Albert répond.
- Vérifier que chaque entrée de `.albert-code/skills.txt` correspond à un skill installé.
- Vérifier que seuls les MCP nécessaires sont activés.
