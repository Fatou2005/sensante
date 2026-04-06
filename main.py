import pandas as pd

# 1. CHARGER LES DONNEES
try:
    df = pd.read_csv('data/patients_dakar.csv', sep=None, engine='python', encoding='latin-1', on_bad_lines='skip')
    print("✅ Fichier chargé avec succès !")
    
    print("-" * 50)
    print("SENSANTE - Exploration du dataset")
    print("-" * 50)

    # 2. DIMENSIONS
    print(f"\nNombre de patients : {len(df)}")
    print(f"Nombre de colonnes : {df.shape[1]}")

    # 3. STATISTIQUES DE BASE
    print("\n--- Statistiques descriptives ---")
    print(df.describe().round(2))

    # 4. RÉPARTITION DES DIAGNOSTICS (Exemple)
    if 'diagnostic' in df.columns:
        print("\n--- Répartition des diagnostics ---")
        diag_counts = df["diagnostic"].value_counts()
        for diag, count in diag_counts.items():
            pct = (count / len(df)) * 100
            print(f"{diag:12s} : {count:3d} patients ({pct:.1f}%)")

    print("\n" + "-" * 50)
    print("Exploration terminée !")
    print("Prochain lab : entraîner un modèle ML")
    print("-" * 50)

except Exception as e:
    print(f"❌ Erreur : {e}")
    