# Retail Strategic Intelligence Dashboard

A high-impact, **Neo-Brutalist Unix-themed** business intelligence application designed to provide executive-level insights into retail performance, inventory segmentation, and seasonal sales trends.

![Dashboard Preview](https://raw.githubusercontent.com/khushalsingh999267/retail-intelligence-dashboard/main/backups/preview.png) *(Note: Add a real preview image to your repo for maximum impact!)*

---

## 🎯 Project Goal
The primary objective of this project is to transform raw retail sales data into actionable strategic intelligence. By leveraging the **ABC Analysis (Pareto Principle)** and **Seasonality Intelligence**, the dashboard empowers decision-makers to optimize inventory, prioritize high-value suppliers, and identify peak revenue windows.

## 🏗️ Implementation & Strategy
The project follows a rigorous 4-stage data science lifecycle:

1.  **Data Engineering**: Automated ingestion of CSV datasets into a structured SQLite database (`retail.db`) with robust cleaning and standardization.
2.  **Feature Engineering**: Derived critical metrics including `Total Sales`, `Season`, `Day of Week`, and `Marketing Impact` flags.
3.  **Advanced Analytics**:
    *   **ABC Segmentation**: Categorizing over 3,000 products into A (High Value), B (Medium), and C (Low) segments based on revenue contribution.
    *   **Seasonality Heatmapping**: Identifying the "Golden Window" for every product category.
4.  **UX/UI Design**: A custom-engineered **Neo-Brutalist** interface using a Unix monospace aesthetic to ensure high readability and a bold, professional "Command Center" feel.

## 💻 Tech Stack & Libraries
*   **Language**: Python 3.10+
*   **Frontend/Dashboard**: [Streamlit](https://streamlit.io/)
*   **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
*   **Database**: [SQLite3](https://www.sqlite.org/index.html)
*   **Visualization**: [Matplotlib](https://matplotlib.org/) (for custom charts) & [Plotly](https://plotly.com/) (for interactive analytics)
*   **Styling**: Custom CSS Injection (Neo-Brutalist & Monospace Unix Theme)

## 📊 Key Insights & Projections
*   **Revenue Concentration**: Identified that **Segment A** (top 27% of products) contributes to **80% of total revenue**, highlighting a critical need for 100% stock availability in these items.
*   **Seasonal Velocity**: Discovered a **"Golden Window"** in the Beer and Wine categories during Summer/Spring, where revenue density spikes by over 40% compared to Winter.
*   **Marketing ROI**: Analyzed marketing activities, revealing a quantifiable "lift" in average transaction value during active campaigns.
*   **Supplier Risk**: Concentrated 60% of revenue across the top 5 suppliers, suggesting a need for strategic renegotiations or diversification.

## 🧠 Skills Gained
*   **Full-Stack Data Engineering**: Building an end-to-end pipeline from raw CSV to live web deployment.
*   **Business Intelligence**: Implementing ABC/Pareto analysis to drive inventory strategy.
*   **Advanced CSS/UX Design**: Creating a unique, high-contrast visual identity using Neo-Brutalist principles.
*   **SQL Database Management**: Optimized querying and storage of high-volume retail transactions.

## 🚀 What Next? (Roadmap)
1.  **Predictive Analytics**: Integrate an ARIMA or Prophet model to forecast sales for Segment A items.
2.  **Supplier Risk Scorecard**: Develop a dynamic rating system for suppliers based on delivery consistency and margins.
3.  **Automated Anomaly Detection**: Implement a system to flag negative sales (returns) or inventory discrepancies in real-time.
4.  **Cloud Migration**: Move the SQLite backend to a cloud-native database like Supabase or PostgreSQL for multi-user support.

---

## 🛠️ How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/khushalsingh999267/retail-intelligence-dashboard.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch the dashboard:
   ```bash
   streamlit run app.py
   ```

---
**Developed by Khushal Singh**  
*Strategic Intelligence for Modern Retail Operations.*
