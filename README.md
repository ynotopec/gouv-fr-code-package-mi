# Skills gouv-fr-code

Quatre skills compacts pour les contraintes propres aux services numériques de l'administration française et à l'environnement gouv-fr-code.

| Skill | Déclenchement |
|---|---|
| `gouv-fr-code-project` | Configurer Albert, OpenCode, agent-vm, les MCP ou la sélection de skills |
| `gouv-fr-code-compliance` | Appliquer ou auditer RGAA, DSFR et RGPD |
| `gouv-fr-code-deploy` | Déployer sur Cloud Pi Native avec Kubernetes, OpenShift et Helm |
| `gouv-fr-code-security` | Manipuler secrets, données sensibles, réseau ou Git depuis agent-vm |

Les conventions génériques de code, Git, lint, API ou monorepo appartiennent au `AGENTS.md` du projet et aux configurations exécutables, pas à des skills chargés en contexte.

## Références standard

Les skills ne recopient pas les méthodes générales déjà portées par un rôle ou
un skill standard. La notation `role:<nom>` désigne une posture à confier à
l'agent et `skill:<nom>` une capacité à charger depuis le catalogue disponible.
Ces références sont des prérequis, pas de nouveaux contenus embarqués dans ce
package. Les instructions qui suivent une référence décrivent uniquement l'écart
propre à gouv-fr-code ou à l'administration française.

## Installation

Installer uniquement les skills nécessaires :

```bash
hermes skill install /path/to/gouv-fr-code-package-mi/gouv-fr-code-compliance
```

Ou copier le dossier concerné dans `~/.hermes/skills/`.

## Validation

Vérifier le manifeste, les métadonnées des skills et les tests avant de proposer
une modification :

```bash
npm run check
```

## Sources de référence

- [Albert API](https://albert.api.etalab.gouv.fr)
- [DSFR](https://www.systeme-de-design.gouv.fr/)
- [RGAA](https://accessibilite.numerique.gouv.fr/)
- [CNIL](https://www.cnil.fr/)
- [Cloud Pi Native](https://cloud-pi-native.fr/)

## Licence

MIT
