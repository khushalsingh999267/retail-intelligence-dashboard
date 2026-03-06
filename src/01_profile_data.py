import pandas as pd
import json
import os

# Paths
CSV_PATH = 'data/Retail and wherehouse Sale.csv'
JSON_PATH = 'data/retail-sales-data-with-seasonal-trends-and-marketing-metadata.json'
REPORT_PATH = 'outputs/data_profile_report.md'

def profile_data():
    print("Step 1: Profiling Data...")
    
    # Load CSV
    df_sales = pd.read_csv(CSV_PATH)
    
    # Load JSON
    with open(JSON_PATH, 'r') as f:
        meta_data = json.load(f)

    # Initial findings
    report = []
    report.append("# Data Profile Report\n")
    report.append("## Dataset Overview\n")
    report.append(f"- **Rows:** {len(df_sales)}")
    report.append(f"- **Columns:** {len(df_sales.columns)}\n")
    
    report.append("## Column Info (CSV)\n")
    col_info = pd.DataFrame({
        'Column': df_sales.columns,
        'Dtype': df_sales.dtypes.astype(str),
        'Missing Values': df_sales.isnull().sum().values
    })
    report.append(col_info.to_markdown(index=False) + "\n")
    
    report.append("## Identified Key Columns\n")
    # Mapping based on dataset structure
    mapping = {
        'Date/Time': 'YEAR, MONTH',
        'Sales/Revenue': 'RETAIL SALES, WAREHOUSE SALES',
        'Profit': 'Not Present (Infer from Sales - Transfers if applicable)',
        'Product': 'ITEM DESCRIPTION, ITEM CODE',
        'Category': 'ITEM TYPE',
        'Customer': 'Not Present',
        'Location/Region': 'Not Present (Supplier as proxy for regional distribution)',
        'Marketing': 'Metadata in JSON (Trends/Seasonality mentioned)'
    }
    for k, v in mapping.items():
        report.append(f"- **{k}:** {v}")
    
    report.append("\n## Sample Data\n")
    report.append(df_sales.head(5).to_markdown(index=False))

    # Save Report
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    with open(REPORT_PATH, 'w') as f:
        f.write("\n".join(report))
    
    print(f"Profiling complete. Report saved to {REPORT_PATH}")

if __name__ == "__main__":
    profile_data()
