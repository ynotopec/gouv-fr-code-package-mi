---
name: gouv-fr-code-compliance
description: Appliquer ou auditer les exigences françaises RGAA, DSFR et RGPD d'un service public numérique. Utiliser pour une interface de l'État, une revue d'accessibilité, l'intégration DSFR ou le traitement de données personnelles.
---

# Vérifier la conformité d'un service public numérique

## Références standard

- `role:accessibility-auditor` pour la méthode d'audit et la restitution des écarts.
- `role:privacy-reviewer` pour l'inventaire et la minimisation des données.
- `skill:design-system` pour l'intégration d'un système de design existant.

## Spécificités françaises

- Identifier les versions applicables du RGAA, du DSFR et les traitements soumis
  au RGPD avant la revue.
- Compléter les contrôles automatisés par les vérifications manuelles du RGAA ;
  ne jamais présenter une revue partielle comme un audit de conformité complet.
- Réutiliser les composants et tokens DSFR officiels avant toute extension et ne
  pas modifier l'identité visuelle sans validation.
- Pour chaque donnée personnelle, documenter finalité, base légale, durée de
  conservation et suppression.
- Ne pas ajouter de traceur tiers sans mécanisme de consentement adapté.
- Ne pas utiliser de données personnelles réelles dans les fixtures, captures ou journaux.
