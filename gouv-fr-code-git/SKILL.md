---
name: gouv-fr-code-git
description: "Gouv-fr-code git conventions: commits, PRs, trailers, gitignore."
version: 0.1.0
author: etalab-ia, Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [gouv-fr-code, git, commits, conventional-commits, pull-request, gitignore, code-review]
    related_skills: [gouv-fr-code, gouv-fr-code-project, gouv-fr-code-security, gouv-fr-code-workflow]
---

# Gouv-fr — Git & Commits

Conventions de gestion de version et hygiène de dépôt pour les applications gouv-fr-code.

## Commits

- Commits atomiques, **Conventional Commits** (`type(scope): …`)
- Types : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Une PR = une intention. Jamais `git push --force`

## Pull Requests

- Une PR = une intention
- Pas de `--force` sur les branches partagées
- Review obligatoire avant merge

## Trailer obligatoire

```
Co-Authored-By: gouv-fr-code (<id>) <noreply@numerique.gouv.fr>
```

## Hygiène de Dépôt

- `.gitignore` avant le 1er commit
- Jamais commité : `node_modules/`, `.venv/`, `vendor/`, secrets, `.env`
