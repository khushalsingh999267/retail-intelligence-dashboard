import pandas as pd
import sqlite3
import re
import os

# Paths
CSV_PATH = 'data/Retail and wherehouse Sale.csv'
DB_PATH = 'retail.db'

def clean_column_name(name):
    # Convert to snake_case
    name = re.sub(r'[^a-zA-Z0-9 ]', '', name)
    return name.strip().lower().replace(' ', '_')

def clean_and_load():
    print("Step 2: Cleaning and Loading Data to SQLite...")
    
    # 1. Load Data
    df = pd.read_csv(CSV_PATH)
    
    # 2. Clean Column Names
    df.columns = [clean_column_name(c) for c in df.columns]
    
    # 3. Data Cleaning
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Convert date components (Year/Month) to a string date format first
    # Many datasets use Month as 1-12
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    
    # Handle missing values
    df['supplier'] = df['supplier'].fillna('UNKNOWN')
    df['retail_sales'] = df['retail_sales'].fillna(0)
    
    # Ensure numeric types
    num_cols = ['retail_sales', 'retail_transfers', 'warehouse_sales']
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # 4. SQLite Database Creation
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Load into table sales_data
    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    
    # 5. Create Indexes
    # (Note: Product corresponds to item_code, Region is not explicitly in dataset)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_date ON sales_data(date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_product ON sales_data(item_code)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_category ON sales_data(item_type)")
    
    conn.commit()
    conn.close()
    print(f"Data cleaned and loaded into {DB_PATH}")

if __name__ == "__main__":
    clean_and_load()
