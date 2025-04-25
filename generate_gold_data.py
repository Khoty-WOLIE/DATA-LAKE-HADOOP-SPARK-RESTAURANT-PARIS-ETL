import pandas as pd

df = pd.read_csv("restaurants_paris.csv")

# Nettoyage : supprimer les restaurants sans nom
df = df[df["name"] != "N/A"]

# Agrégation : nombre de fois qu'un nom de restaurant apparaît
agg = df["name"].value_counts().reset_index()
agg.columns = ["restaurant_name", "count"]

agg.to_csv("restaurants_gold.csv", index=False)
print("Fichier gold généré : restaurants_gold.csv")

