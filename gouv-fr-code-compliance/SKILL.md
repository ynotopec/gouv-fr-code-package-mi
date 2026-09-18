---
name: gouv-fr-code-compliance
description: Appliquer ou auditer les exigences françaises RGAA, DSFR et RGPD d'un service public numérique. Utiliser pour une interface de l'État, une revue d'accessibilité, l'intégration DSFR ou le traitement de données personnelles.
---

# Vérifier la conformité d'un service public numérique

## Procédure

1. Identifier les référentiels applicables au service : RGAA, DSFR et traitements soumis au RGPD.
2. Réutiliser les composants et tokens DSFR officiels avant de créer un composant personnalisé.
3. Tester les parcours complets au clavier, l'ordre du focus, les intitulés, les alternatives textuelles et la structure HTML.
4. Compléter les tests automatisés par une vérification manuelle ; ne jamais conclure à la conformité RGAA sur le seul résultat d'un outil.
5. Pour chaque donnée personnelle, documenter la finalité et supprimer les collectes non nécessaires.
6. Signaler les écarts, leur impact utilisateur et la preuve permettant de les reproduire.

## Garde-fous

- Ne pas remplacer un élément HTML natif par ARIA lorsque le natif convient.
- Ne pas modifier l'identité visuelle ou les composants DSFR sans justification validée.
- Ne pas ajouter de traceur tiers sans mécanisme de consentement adapté.
- Ne pas utiliser de données personnelles réelles dans les fixtures, captures ou journaux.
- Ne pas présenter une revue partielle comme un audit réglementaire complet.

## Vérification

- Parcourir sans souris toutes les fonctions principales.
- Contrôler contraste, zoom, erreurs de formulaire et annonces des contenus dynamiques.
- Rechercher les couleurs et espacements codés en dur hors tokens DSFR.
- Inventorier les données collectées, leur finalité, leur conservation et leur suppression.
- Produire une liste d'écarts traçable plutôt qu'un verdict sans preuves.
