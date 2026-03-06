# Project Context: Retail Sales Data Analysis

## Overview
This project involves analyzing a retail sales dataset with seasonal trends and marketing metadata.

## Data Sources
- `retail-sales-data-with-seasonal-trends-and-marketing-metadata.json`: Croissant metadata.
- `archive.zip`: Original compressed dataset.
- `Retail and wherehouse Sale.csv`: The primary dataset (extracted from `archive.zip`).
  - **Rows:** 30,002
  - **Key Columns:** `YEAR`, `MONTH`, `SUPPLIER`, `ITEM CODE`, `ITEM DESCRIPTION`, `ITEM TYPE`, `RETAIL SALES`, `RETAIL TRANSFERS`, `WAREHOUSE SALES`.

## Conversation History & Decisions
- **2026-03-05**: Initialized project. Extracted `Retail and wherehouse Sale.csv` from `archive.zip`. Created `GEMINI.md`.
- **2026-03-05**: Performed initial data quality check and generated profile report.
- **2026-03-05**: Completed ABC Segmentation Analysis. Identified Segment A (834 items, 80% revenue). Generated `outputs/comprehensive_report.md`.

## Future Tasks
- [x] Data profiling and quality assessment.
- [x] Segmentation analysis: ABC Analysis of product performance.
- [ ] Exploratory Data Analysis (EDA): Visualize sales trends across months and years.
- [ ] Analyze seasonal patterns in `RETAIL SALES` vs `WAREHOUSE SALES`.
- [ ] Investigate negative sales values (returns) and outliers.
