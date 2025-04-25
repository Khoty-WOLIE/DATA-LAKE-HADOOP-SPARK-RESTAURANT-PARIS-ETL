import pandas as pd

# Charger le fichier CSV local (copie depuis HDFS à faire au préalable)
df = pd.read_csv("users_clean.csv")

# Calculer la moyenne d’âge
mean_age = df["age"].mean()

# Ajouter une colonne "age_group"
df["age_group"] = df["age"].apply(lambda x: "young" if x < 30 else "adult")

# Sauvegarder le résultat dans un nouveau fichier
df.to_csv("users_analytics.csv", index=False)

print(f"Moyenne d’âge : {mean_age}")

