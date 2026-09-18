# Package Gouv-fr-code pour Hermes Agent

Package complet pour construire des applications de l'administration française avec Hermes Agent.

## Contenu

| Directory | Rôle |
|---|---|
| `gouv-fr-code/` | Index général du package |
| `gouv-fr-code-project/` | Structure du projet, layout, OpenCode, variables d'environnement |
| `gouv-fr-code-security/` | Règles de sécurité : secrets, gitleaks, SQL injection, TLS, VM isolation |
| `gouv-fr-code-compliance/` | RGAA (accessibilité), DSFR (design system), RGPD |
| `gouv-fr-code-workflow/` | Plan mode, task management, self-improvement, bug fixing |
| `gouv-fr-code-git/` | Commits Conventional, PRs, trailer Co-Authored-By, .gitignore |

## Installation

Chaque dossier contient un `SKILL.md`. Pour installer un skill :

```bash
hermes skill install /path/to/gouv-fr-code-package/gouv-fr-code
```

Ou copier manuellement les dossiers dans `~/.hermes/skills/`.

## Ressources

- **Source** : `github.com/etalab-ia/albert-code`
- **OpenCode** : `https://opencode.ai/docs/fr`
- **Albert API** : `https://albert.api.etalab.gouv.fr`
- **DSFR** : `https://www.systeme-de-design.gouv.fr/`
- **Skills of the State** : `https://github.com/etalab-ia/skills`

## License

MIT — Auteur : gouv-fr-code (etalab-ia), Hermes Agent
