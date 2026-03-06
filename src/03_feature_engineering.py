import pandas as pd
import sqlite3

def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

def engineer_features():
    print("Step 3: Engineering Features...")
    
    conn = sqlite3.connect('retail.db')
    df = pd.read_sql("SELECT * FROM sales_data", conn)
    
    # 1. Date Features
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_week'] = df['date'].dt.day_name()
    df['season'] = df['month'].apply(get_season)
    
    # 2. Financial Metrics
    # In this dataset, we can define total_sales = retail_sales + warehouse_sales
    df['total_sales'] = df['retail_sales'] + df['warehouse_sales']
    
    # 3. Marketing Flag (Hypothetical)
    # Marketing campaigns are often active during holiday seasons (Winter/Summer)
    df['marketing_active'] = df['season'].apply(lambda x: 1 if x in ['Winter', 'Summer'] else 0)
    
    # 4. Save to SQLite
    df.to_sql('enriched_sales', conn, if_exists='replace', index=False)
    
    conn.close()
    print("Feature engineering complete. Enriched data saved to table 'enriched_sales'.")

if __name__ == "__main__":
    engineer_features()
