# Skills gouv-fr-code

Quatre skills compacts pour les contraintes propres aux services numériques de l'administration française et à l'environnement gouv-fr-code.

| Skill | Déclenchement |
|---|---|
| `gouv-fr-code-project` | Configurer Albert, OpenCode, agent-vm, les MCP ou la sélection de skills |
| `gouv-fr-code-compliance` | Appliquer ou auditer RGAA, DSFR et RGPD |
| `gouv-fr-code-deploy` | Déployer sur Cloud Pi Native avec Kubernetes, OpenShift et Helm |
| `gouv-fr-code-security` | Manipuler secrets, données sensibles, réseau ou Git depuis agent-vm |

Les conventions génériques de code, Git, lint, API ou monorepo appartiennent au `AGENTS.md` du projet et aux configurations exécutables, pas à des skills chargés en contexte.

## Installation

Installer uniquement les skills nécessaires :

```bash
hermes skill install /path/to/gouv-fr-code-package-mi/gouv-fr-code-compliance
```

Ou copier le dossier concerné dans `~/.hermes/skills/`.

## Sources de référence

- [Albert API](https://albert.api.etalab.gouv.fr)
- [DSFR](https://www.systeme-de-design.gouv.fr/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)
- [CNIL](https://www.cnil.fr/)
- [Cloud Pi Native](https://cloud-pi-native.fr/)

## Licence

MIT
