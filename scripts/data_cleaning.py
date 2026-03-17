import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv('data/raw/superstore.csv')

# Nettoyage
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df = df.dropna(subset=['sales', 'profit', 'order_id'])

# Conversion des dates
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

# Feature engineering
df['profit_margin'] = np.where(
    df['sales'] != 0,
    df['profit'] / df['sales'],
    0
)

df['shipping_delay'] = (df['ship_date'] - df['order_date']).dt.days

df['discount_level'] = pd.cut(
    df['discount'],
    bins=[-1, 0, 0.2, 0.5, 1],
    labels=['No Discount', 'Low', 'Medium', 'High']
)

# Vérification
print(df.info())
print(df.describe())

# Export
df.to_csv('data/processed/superstore_cleaned.csv', index=False)

print('Nettoyage terminé.')