import pandas as pd
import numpy as np

print("🚀 Début du nettoyage...")

# Charger les données
df = pd.read_csv('data/raw/superstore.csv')

# -----------------------------
# 🧹 Nettoyage de base
# -----------------------------
df.columns = df.columns.str.strip()
df = df.drop_duplicates()

# -----------------------------
# 🔢 Nettoyage + conversion des colonnes numériques
# -----------------------------
numeric_cols = ['sales', 'profit', 'discount', 'quantity', 'shipping_cost']

for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(',', '').str.strip()
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Vérification des types
print("\n📊 Types après conversion :")
print(df[numeric_cols].dtypes)

# Suppression des lignes invalides
df = df.dropna(subset=['sales', 'profit', 'order_id'])

# -----------------------------
# 📅 Conversion des dates
# -----------------------------
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce')

# -----------------------------
# 🧠 Feature engineering
# -----------------------------

# Profit margin (sécurisé)
df['profit_margin'] = np.where(
    df['sales'] != 0,
    df['profit'] / df['sales'],
    0
)

# Délai de livraison
df['shipping_delay'] = (df['ship_date'] - df['order_date']).dt.days

# Catégorisation des discounts
df['discount_level'] = pd.cut(
    df['discount'],
    bins=[-1, 0, 0.2, 0.5, 1],
    labels=['No Discount', 'Low', 'Medium', 'High']
)

# -----------------------------
# 🔍 Vérifications
# -----------------------------
print("\n📊 INFO DATAFRAME")
print(df.info())

print("\n📈 STATISTIQUES")
print(df.describe())

print("\n❗ Valeurs manquantes :")
print(df.isna().sum())

# -----------------------------
# 💾 Export
# -----------------------------
df.to_csv('data/processed/superstore_cleaned.csv', index=False)

print("\n✅ Nettoyage terminé ! Fichier généré dans data/processed/")