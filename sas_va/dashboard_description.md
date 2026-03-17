# Description du Dashboard SAS Visual Analytics

## Pages et visuels principaux

1. **Vue d’ensemble**
   - KPIs : Total Sales, Total Profit, Total Quantity, Profit Margin
   - Filtres : Année, Marché, Catégorie

2. **Analyse géographique**
   - Carte : Sales et Profit par country
   - Bar chart : Sales par market
   - Bar chart : Profit par région

3. **Analyse produit**
   - Bar chart : Sales par category
   - Table : Top 10 produits
   - Table : Produits avec profit négatif

4. **Impact des remises**
   - Scatter plot : Discount vs Profit

5. **Analyse client**
   - Pie chart : Segment
   - Bar chart : Sales par segment

6. **Analyse logistique**
   - Bar chart : Ship mode
   - Scatter plot : Shipping cost vs Profit

## Interactivité
- Filtres globaux : Année, Marché, Région, Catégorie
- Drill-down sur les visuels

## Données utilisées
- Fichier : data/processed/superstore_cleaned.csv
- Colonnes clés : sales, profit, discount, category, market, region, segment, order_date
