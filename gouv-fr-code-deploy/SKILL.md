---
name: gouv-fr-code-deploy
description: Préparer ou auditer le déploiement d'un service gouv-fr-code sur Cloud Pi Native, Kubernetes ou OpenShift. Utiliser pour adapter un conteneur ou un chart Helm aux contraintes rootless et de moindre privilège de la plateforme.
---

# Déployer sur Cloud Pi Native

## Procédure

1. Construire une image reproductible avec une version de base épinglée et un build multi-stage.
2. Exécuter le service avec un UID non-root et écouter sur un port non privilégié.
3. Déclarer dans Kubernetes les ressources, probes et paramètres nécessaires au démarrage.
4. Appliquer un `securityContext` compatible Kubernetes et OpenShift :

```yaml
securityContext:
  runAsNonRoot: true
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop: [ALL]
```

5. Injecter la configuration et les secrets au déploiement ; ne jamais les embarquer dans l'image ou `values.yaml`.
6. Valider le rendu Helm avant toute livraison sur Cloud Pi Native.

## Points d'attention

- Prévoir explicitement les répertoires inscriptibles requis, notamment `/tmp`, lorsque le système de fichiers racine est en lecture seule.
- Ne pas dépendre d'un UID fixe si la politique OpenShift en attribue un dynamiquement.
- Ne pas utiliser le tag `latest`.
- Conserver les réglages propres à chaque environnement hors du chart commun.

## Vérification

```bash
docker build -t app:test .
helm lint ./helm
helm template app ./helm
```

Vérifier ensuite les probes, l'arrêt gracieux, le démarrage rootless et l'absence de secret dans le rendu.
