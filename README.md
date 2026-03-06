# Retail Analytics Portfolio Project

## Project Overview
This project is an end-to-end retail analytics pipeline designed for a Data & Analytics placement role. It demonstrates skills in data engineering, SQL, Python analysis, and dashboarding using a retail sales dataset.

## Skills Demonstrated
- **Data Engineering:** Cleaning and loading raw CSV/JSON data into a SQLite database.
- **SQL Analytics:** Complex queries for KPI tracking, trend analysis, and seasonality.
- **Python Data Analysis:** Automated data profiling, feature engineering, and ABC segmentation.
- **Data Visualization:** Interactive Streamlit dashboard with Plotly charts.
- **Automation:** A shell-based pipeline to process data from raw to insight.

## Architecture
1. **Data Layer:** Raw CSV and JSON metadata in `data/`.
2. **Processing Layer:** Python scripts in `src/` for profiling, cleaning, feature engineering, and segmentation.
3. **Storage Layer:** SQLite database (`retail.db`) with optimized indexes.
4. **Analytics Layer:** SQL queries in `sql/` for business insights.
5. **Presentation Layer:** Streamlit application (`app.py`) for stakeholders.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the full data pipeline:
   ```bash
   chmod +x run_pipeline.sh
   ./run_pipeline.sh
   ```
3. Launch the dashboard:
   ```bash
   streamlit run app.py
   ```

## Example Business Insights
- **Seasonality:** Sales peak during Winter and Summer, suggesting marketing campaigns are effectively aligned with holiday trends.
- **Product Strategy:** ABC analysis reveals that a small fraction of products (Segment A) drives 80% of revenue, highlighting key items for inventory focus.
- **Supplier Performance:** Top suppliers contribute significantly to warehouse movement, indicating strong partnerships for high-volume items.

## Future Improvements
- **Predictive Analytics:** Implement a forecasting model for next-month sales.
- **Customer Segmentation:** If customer IDs become available, perform RFM (Recency, Frequency, Monetary) clustering.
- **Automated Reporting:** Integrate an email alert system for low-performing product categories.
