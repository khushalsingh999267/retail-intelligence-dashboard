import pandas as pd
import sqlite3
import os

def segment_products():
    print("Step 4: Performing Segmentation Analysis...")
    
    conn = sqlite3.connect('retail.db')
    df = pd.read_sql("SELECT * FROM enriched_sales", conn)
    
    # ABC Analysis based on total_sales
    # Group by item_description
    product_sales = df.groupby('item_description')['total_sales'].sum().reset_index()
    product_sales = product_sales.sort_values(by='total_sales', ascending=False)
    
    # Calculate cumulative percentage
    product_sales['cumulative_sales'] = product_sales['total_sales'].cumsum()
    total_revenue = product_sales['total_sales'].sum()
    product_sales['revenue_share'] = product_sales['cumulative_sales'] / total_revenue
    
    # Assign Segments
    def assign_abc(share):
        if share <= 0.8: return 'A' # Top 80% revenue
        elif share <= 0.95: return 'B' # Next 15%
        else: return 'C' # Bottom 5%
        
    product_sales['segment'] = product_sales['revenue_share'].apply(assign_abc)
    
    # Save Results
    if not os.path.exists('outputs'): os.makedirs('outputs')
    product_sales.to_csv('outputs/product_segments.csv', index=False)
    
    # Generate Insights
    insights = f"""# Segmentation Analysis Insights

## Product ABC Analysis Results
- **Segment A (High Value):** {len(product_sales[product_sales['segment'] == 'A'])} products contribute to 80% of total sales.
- **Segment B (Medium Value):** {len(product_sales[product_sales['segment'] == 'B'])} products contribute to the next 15% of sales.
- **Segment C (Low Value):** {len(product_sales[product_sales['segment'] == 'C'])} products contribute to the final 5% of sales.

## Business Insights
1. **Focus on Segment A:** A small group of products drives the vast majority of revenue. Inventory management should prioritize these items to prevent stockouts.
2. **Optimize Segment C:** There is a long tail of low-performing products. Consider reducing variety in this segment to save on storage and administrative costs.
3. **Suppliers of A-Grade items:** {', '.join(df[df['item_description'].isin(product_sales[product_sales['segment'] == 'A']['item_description'])]['supplier'].unique()[:3])} are key partners.
"""
    with open('outputs/segmentation_insights.md', 'w') as f:
        f.write(insights)
        
    conn.close()
    print("Segmentation analysis complete. Results saved to outputs/.")

if __name__ == "__main__":
    segment_products()
