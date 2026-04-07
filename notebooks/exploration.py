import pandas as pd

# Charger les données
df = pd.read_excel("data/patients_dakar.csv")
# Analyse initiale
print("Nombre de patients:", df.shape[0])
print("\nAperçu des données:")
print(df.head())

# Exercice 1 : Analyse par sexe et diagnostic
print("\nNombre de patients par sexe et diagnostic:")
print(df.groupby(["sexe", "diagnostic"]).size())