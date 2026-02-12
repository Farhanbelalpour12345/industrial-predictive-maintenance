# 🏭 Système Industriel de Maintenance Prédictive basé sur des Données Capteurs

Projet complet de Data Science & Data Engineering simulant un système industriel de surveillance de machines.

---

## 🎯 Objectif du projet

Dans l’industrie moderne, les machines sont équipées de nombreux capteurs.  
L’objectif est d’exploiter ces données afin de :

- 🔍 Détecter les anomalies
- ⏳ Prédire la durée de vie restante (RUL – Remaining Useful Life)
- 📊 Surveiller la performance du modèle
- 📉 Détecter la dérive des données (Data Drift)
- 💰 Simuler l’impact financier des décisions de maintenance
- 🧠 Expliquer les décisions du modèle (Explainability)

Ce projet adopte une approche **orientée production**, et non simplement un notebook académique.

---

## 🏗 Architecture du système

```
Données brutes → Pipeline de traitement → Feature Engineering
               → Modèles ML (RUL + Anomalies)
               → Base PostgreSQL
               → Dashboard Streamlit
               → Monitoring & Drift
```

---

## 🛠 Stack Technique

- Python
- Pandas / NumPy
- Scikit-Learn
- PostgreSQL
- SQLAlchemy
- Streamlit
- Docker & Docker Compose
- Joblib (versionnement des modèles)

---

## 📂 Structure du projet

```
industrial-predictive-maintenance/
│
├── src/
│   ├── ingestion/
│   ├── processing/
│   ├── features/
│   ├── models/
│   ├── database/
│   └── config/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🔁 Pipeline de traitement des données

Le pipeline réalise :

1. Chargement du dataset NASA Turbofan
2. Nettoyage et normalisation
3. Feature engineering (rolling mean & std)
4. Détection d’anomalies (Isolation Forest)
5. Création de la cible RUL
6. Sauvegarde en CSV
7. Enregistrement dans PostgreSQL

Exécution :

```bash
docker exec -it predictive_app python -m src.processing.run_full_pipeline
```

---

## 🤖 Modélisation Machine Learning

### 1️⃣ Prédiction du RUL (Random Forest Regressor)

- Prédit la durée de vie restante des machines
- Sauvegarde :
  - CSV
  - Base PostgreSQL (`rul_predictions`)
- Versionnement automatique du modèle
- Enregistrement des métriques (MAE, RMSE) dans la table `model_metrics`

Exécution :

```bash
docker exec -it predictive_app python -m src.models.rul_regression
```

---

### 2️⃣ Détection d’anomalies

- Basée sur Isolation Forest
- Génère :
  - Score d’anomalie
  - Indicateur binaire anomalie / normal

---

## 📊 Fonctionnalités du Dashboard

### 🏭 Analyse Machine
- Visualisation du RUL
- Évolution des capteurs
- Classement des machines à risque

### 📉 Monitoring & Data Drift
- Comparaison des statistiques entre données d’entraînement et données courantes
- Score de dérive par variable
- Indicateur global de santé du modèle

### 💰 Simulation d’Impact Business

Permet de simuler :

- Seuil critique de RUL
- Coût d’une panne
- Coût d’une maintenance préventive

Le système calcule si la stratégie préventive est économiquement justifiée.

👉 Cette partie transforme un modèle ML en outil d’aide à la décision industrielle.

### 🧠 Explainability

- Importance des variables (Random Forest)
- Identification des capteurs influents
- Justification des prédictions auprès d’un décideur industriel

---

## 🗄 Tables en base de données

| Table | Description |
|--------|-------------|
| processed_data | Dataset final traité |
| rul_predictions | Prédictions du modèle |
| model_metrics | Historique des performances |
| training_feature_stats | Statistiques d’entraînement pour drift |

---

## 🐳 Déploiement avec Docker

Lancement complet du système :

```bash
docker compose up --build
```

Accès au dashboard :

```
http://localhost:8501
```

---

## 🚀 Concepts avancés implémentés

- Versionnement de modèles
- Monitoring des performances
- Détection de dérive
- Simulation d’impact financier
- Architecture conteneurisée
- Logging en base
- Approche orientée production

---

## 📌 Pourquoi ce projet est différenciant ?

La plupart des projets ML s’arrêtent à :

> "J’ai entraîné un modèle avec MAE = X"

Ce projet démontre :

- Une vision industrielle
- Une compréhension business
- Une approche Data Engineering
- Une réflexion monitoring & observabilité
- Une capacité de mise en production

---

## 👤 Auteur

Projet réalisé par Mohammad BELALPOUR  
Data Science & Machine Learning Engineering.
