#!/bin/bash

echo "Starting Retail Analytics Pipeline..."

# Run profiling
python3 src/01_profile_data.py

# Run cleaning and DB load
python3 src/02_clean_and_load_sqlite.py

# Run feature engineering
python3 src/03_feature_engineering.py

# Run segmentation analysis
python3 src/04_segmentation_analysis.py

echo "Pipeline complete. You can now launch the dashboard with:"
echo "streamlit run app.py"
