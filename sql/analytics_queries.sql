-- KPI Summary
-- Calculates Total Sales (Retail + Warehouse) and Total Rows (Proxy for Orders)
SELECT 
    COUNT(*) as total_records,
    SUM(retail_sales) as total_retail_revenue,
    SUM(warehouse_sales) as total_warehouse_revenue,
    SUM(retail_sales + warehouse_sales) as total_combined_revenue
FROM enriched_sales;

-- Revenue Trend by Month
-- Analyzes monthly performance to identify seasonal growth
SELECT 
    year, 
    month, 
    SUM(retail_sales + warehouse_sales) as monthly_revenue
FROM enriched_sales
GROUP BY year, month
ORDER BY year, month;

-- Top 5 Categories by Revenue
-- Identifies the most profitable business segments
SELECT 
    item_type, 
    SUM(retail_sales + warehouse_sales) as category_revenue
FROM enriched_sales
GROUP BY item_type
ORDER BY category_revenue DESC
LIMIT 5;

-- Seasonality Analysis
-- Evaluates sales performance during defined seasons
SELECT 
    season, 
    AVG(retail_sales + warehouse_sales) as avg_seasonal_sales,
    SUM(retail_sales + warehouse_sales) as total_seasonal_sales
FROM enriched_sales
GROUP BY season
ORDER BY total_seasonal_sales DESC;

-- Marketing Campaign Impact (Hypothetical)
-- Compares sales when marketing_active = 1 vs 0
SELECT 
    marketing_active, 
    SUM(retail_sales + warehouse_sales) as total_revenue,
    AVG(retail_sales + warehouse_sales) as avg_sales_per_record
FROM enriched_sales
GROUP BY marketing_active;

-- Supplier Distribution
-- Top 10 Suppliers by revenue contribution
SELECT 
    supplier, 
    SUM(retail_sales + warehouse_sales) as supplier_revenue
FROM enriched_sales
GROUP BY supplier
ORDER BY supplier_revenue DESC
LIMIT 10;
