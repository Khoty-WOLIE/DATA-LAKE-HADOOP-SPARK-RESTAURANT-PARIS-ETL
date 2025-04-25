# DATA-LAKE-HADOOP-SPARK-RESTAURANT-PARIS-ETL
Projet d’architecture Data Lake local avec traitement distribué et analyse des données OSM via WSL sous Windows, avec HDFS, Hive, Spark SQL, et visualisation des données dans Jupyter Notebook.

---

## 🚀 Objectif

Mettre en œuvre un **Data Lake fonctionnel** avec la stack suivante :
- **Hadoop HDFS** : stockage distribué local
- **Hive** : traitement SQL (optionnel)
- **Spark SQL** : traitement analytique performant
- **PySpark + Pandas** : analyse programmée en Python
- **Jupyter Notebook** : visualisation de données
- **Bronze / Silver / Gold layers** : architecture analytique

---

## 📁 Architecture en locale

```bash
📂 hadoop_datalake
├── hadoop-3.4.1/         # Hadoop HDFS
├── hive/                 # Hive 3.1.3 (optionnel)
├── spark/                # Spark 3.5.0
├── notebooks/
│   └── Analyse_Restaurants_Paris.ipynb  # Notebook principal ✅
├── restaurants_gold.csv  # Données exportées pour analyse
```

---

## 🧱 Étapes réalisées

### 🔧 Setup Environnement

- [x] WSL (Ubuntu 22.04) + Java 8
- [x] Installation de Hadoop 3.4.1
- [x] Configuration HDFS + formatage `namenode`
- [x] Lancement manuel des démons `namenode` et `datanode`
- [x] Interface Web HDFS sur `http://localhost:9870`

---

### 🗃️ Structure Data Lake

- [x] 📦 **Bronze** : fichiers `.osm` OpenStreetMap
- [x] 🧼 **Silver** : extraction des restaurants → `.csv`
- [x] 📊 **Gold** : agrégation, analyse, transformation

---

### 🐘 Hive (facultatif)

- [x] Hive 3.1.3 installé
- [x] Table externe sur fichier HDFS
- [x] Requêtes SQL simples (`SELECT`, `LIMIT`)
- [ ] ❌ MapReduce local instable sur WSL (utilisé Spark SQL à la place)

---

### ⚡ Spark SQL

- [x] Spark 3.5.0 installé
- [x] Lecture du CSV depuis HDFS
- [x] Requêtes SQL complexes (`GROUP BY`, `ORDER BY`)
- [x] Export en Parquet
- [x] Utilisation de PySpark + Spark SQL

---

### 📓 Jupyter Notebook

- [x] Lancement via Anaconda
- [x] Lecture du fichier `restaurants_gold.csv`
- [x] Analyse exploratoire avec `pandas`
- [x] Visualisation avec `seaborn`, `matplotlib`
- [x] Statistiques descriptives
- [x] Graphique des restaurants les plus fréquents

---

## 🔜 Autre étapes

### 📊 Connexions BI / visualisation

- [ ] **Apache Superset**
  - Connexion via Hive ou Parquet
  - Table interactive et dashboards
- [ ] **Power BI**
  - Lecture CSV/Parquet depuis HDFS (via `hadoop fs -copyToLocal`)
  - Ou connexion directe Hive via ODBC
- [ ] **Extension Notebook**
  - Visualisation sur carte avec `folium` ou `geopandas`
  - Clustering avec `scikit-learn`

---

## 🧠 Technologies utilisées

| Outil         | Version       | Rôle                               |
|---------------|---------------|------------------------------------|
| Hadoop        | 3.4.1         | Stockage HDFS                      |
| Hive          | 3.1.3         | SQL sur fichiers HDFS (optionnel)  |
| Spark         | 3.5.0         | Traitement distribué et SQL        |
| PySpark       | incl. Spark   | Requêtes et transformation Python  |
| Python        | 3.10+         | Parsing, visualisation, notebooks  |
| Jupyter       | via Anaconda  | Notebook interactif                |
| Java          | 8 (OpenJDK)   | Support Hadoop / Hive / Spark      |

---

## 📦 Librairies Python utilisées

```bash
pandas
seaborn
matplotlib
pyspark
findspark
```

---

## 📄 Notebook principal

🔗 Fichier : [`notebooks/Analyse_Restaurants_Paris.ipynb`](https://github.com/Khoty-WOLIE/DATA-LAKE-HADOOP-SPARK-RESTAURANT-PARIS-ETL/blob/main/Analyse%20des%20restaurants%20Parisiens.ipynb)

Contenu :
- Chargement des données depuis CSV
- Statistiques descriptives
- Distribution des restaurants
- Top 10 des noms les plus fréquents
- Analyse textuelle des noms

---

## 🛠️ Commandes utiles

```bash
# Lancer Hadoop
hdfs --daemon start namenode
hdfs --daemon start datanode

# Lire un fichier depuis HDFS
hdfs dfs -cat /datalake/gold/paris/restaurants_gold.csv

# Lancer Spark SQL
spark-sql

# Lancer PySpark
pyspark
```

---

## 📌 Notes

- ⚠️ Hive sur WSL ne supporte pas bien MapReduce → Spark SQL préféré
- ✅ Spark SQL fonctionne parfaitement pour les requêtes complexes
- 📈 Jupyter permet une visualisation rapide et fluide
- 🔐 Tous les fichiers sont stockés dans `/datalake` sur HDFS

---

## 📷 Captures possibles

- Interface HDFS (http://localhost:9870)
- Web UI de Spark (`http://localhost:4040`)
- Graphiques matplotlib / seaborn du notebook

---

## 🤝 Crédits & Inspiration

- [OpenStreetMap](https://www.openstreetmap.org/)
- [Apache Hadoop](https://hadoop.apache.org/)
- [Apache Spark](https://spark.apache.org/)
- [Hive](https://hive.apache.org/)
