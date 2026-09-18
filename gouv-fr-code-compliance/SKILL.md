---
name: gouv-fr-code-compliance
description: "Gouv-fr-code compliance: RGAA accessibility, DSFR design system, RGPD data protection."
version: 0.1.0
author: etalab-ia, Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [gouv-fr-code, compliance, rgaa, dsfr, rgpd, accessibility, etat, design-system, data-protection]
    related_skills: [gouv-fr-code, gouv-fr-code-project, gouv-fr-code-security]
---

# Gouv-fr — Conformité

Règles d'accessibilité et conformité réglementaire pour les applications gouv-fr-code.

## RGAA (Accessibilité)

- Contraste suffisant (WCAG AA minimum)
- Navigation complète au clavier
- Attributs `alt` pertinents sur les images
- Structure sémantique HTML (headings, landmarks)
- Rôles ARIA quand nécessaire
- Tests d'accessibilité automatisés dans la CI

## DSFR (Design System de l'État)

- Utiliser les composants officiels DSFR (React, Vue, HTML/CSS)
- Respecter les tokens (couleurs, tailles, espacements)
- Ne pas customiser sans validation
- Components : boutons, champs de formulaire, tableaux, pagination, toasts, modals

## RGPD (Protection des données)

- Minimisation des données collectées
- Pas de traceur tiers sans consentement
- Consentement explicement recueilli
- Droit à l'oubli : suppression des données utilisateur
- Chiffrement des données sensibles

## Checklist de conformité

Avant de livrer :
- [ ] Contraste validé (WCAG AA)
- [ ] Navigation clavier testée
- [ ] DSFR tokens utilisés (pas de couleurs custom)
- [ ] Aucun secret en production
- [ ] RGPD : pas de données personnelles non justifiées
- [ ] Tests d'accessibilité passent
