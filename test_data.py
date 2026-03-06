import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect('retail.db')

def load_data():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM enriched_sales", conn)
    df['date'] = pd.to_datetime(df['date'])
    category_map = {
        'KEGS': 'DRAUGHT BEER',
        'STR_SUPPLIES': 'STORE SUPPLIES',
        'REF': 'REFRIGERATED',
        'DUNNAGE': 'SHIPPING MATERIALS'
    }
    df['item_type'] = df['item_type'].replace(category_map)
    df = df.rename(columns={
        'year': 'Year',
        'item_type': 'Category',
        'total_sales': 'Total Sales ($)',
        'supplier': 'Supplier',
        'season': 'Season',
        'date': 'Transaction Date',
        'marketing_active': 'Marketing Campaign'
    })
    df['Marketing Campaign'] = df['Marketing Campaign'].map({1: 'Active', 0: 'Inactive'})
    conn.close()
    return df

df = load_data()
print(f"Total rows: {len(df)}")
print(f"Categories: {df['Category'].unique()[:5]}")

years = sorted(df['Year'].unique())
seasons = df['Season'].unique()
categories = df['Category'].unique()[:5]

filtered_df = df.copy()
filtered_df = filtered_df[filtered_df['Total Sales ($)'] >= 0]
filtered_df = filtered_df[filtered_df['Year'].isin(years)]
filtered_df = filtered_df[filtered_df['Season'].isin(seasons)]
filtered_df = filtered_df[filtered_df['Category'].isin(categories)]

print(f"Filtered rows: {len(filtered_df)}")
print(filtered_df['Total Sales ($)'].describe())
