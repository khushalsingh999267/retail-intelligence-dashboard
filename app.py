import streamlit as st
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

# ---------------------------------------------------
# 1. PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Retail Strategic Intelligence",
    layout="wide"
)

# ---------------------------------------------------
# 2. STYLING
# ---------------------------------------------------
st.markdown("""
<style>
/* Base app */
html, body, .stApp {
    font-family: 'Courier New', Courier, monospace !important;
    color: #000000 !important;
    background-color: #FFFFFF !important;
}

/* Move sidebar to right */
[data-testid="stAppViewContainer"] {
    flex-direction: row-reverse !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFFF00 !important;
    border-left: 4px solid #000000 !important;
    border-right: none !important;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    font-family: 'Courier New', Courier, monospace !important;
    color: #000000 !important;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    border: 2px solid #000000 !important;
    border-radius: 0px !important;
    box-shadow: 4px 4px 0px 0px #000000 !important;
    background-color: #FFFFFF !important;
}

/* Horizontal rule */
hr {
    border: 2px solid #000000 !important;
    opacity: 1 !important;
}

/* Alerts / info / success / warning boxes */
div[data-testid="stAlert"] {
    border: 3px solid #000000 !important;
    box-shadow: 6px 6px 0px 0px #000000 !important;
    border-radius: 0px !important;
}

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] li {
    font-family: 'Courier New', Courier, monospace !important;
    font-size: 20px !important;
}

/* Tables */
div[data-testid="stTable"] table,
div[data-testid="stDataFrame"] {
    border: 3px solid #000000 !important;
    box-shadow: 8px 8px 0px 0px #000000 !important;
    border-radius: 0px !important;
}

/* Bold labels used in normal page content */
div[data-testid="stMarkdownContainer"] > p > strong {
    font-size: 28px !important;
    font-weight: 900 !important;
    text-transform: uppercase !important;
}

/* Custom title */
.neo-title {
    font-size: 56px;
    font-weight: 950;
    text-transform: uppercase;
    letter-spacing: -2px;
    line-height: 1;
    margin-bottom: 30px;
}

/* Custom section header */
.neo-section {
    font-size: 36px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: -1px;
    margin-top: 18px;
    margin-bottom: 18px;
    line-height: 1.1;
}

/* KPI card */
.neo-metric-card {
    background-color: #00FFFF;
    border: 3px solid #000000;
    padding: 18px 18px 14px 18px;
    box-shadow: 8px 8px 0px 0px #000000;
    border-radius: 0px;
    min-height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.neo-metric-label {
    font-size: 22px;
    font-weight: 900;
    text-transform: uppercase;
    line-height: 1.2;
    margin-bottom: 10px;
}

.neo-metric-value {
    font-size: 44px;
    font-weight: 950;
    line-height: 1;
}

/* ABC explainer card */
.neo-explainer {
    background-color: #FFF6CC;
    border: 3px solid #000000;
    box-shadow: 6px 6px 0px 0px #000000;
    padding: 16px 18px;
    margin-bottom: 20px;
}

.neo-explainer-title {
    font-size: 22px;
    font-weight: 900;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.neo-explainer-text {
    font-size: 18px;
    line-height: 1.6;
}

/* Expander styled like the rest of the dashboard */
.streamlit-expanderHeader {
    border: 3px solid #000000 !important;
    box-shadow: 6px 6px 0px 0px #000000 !important;
    border-radius: 0px !important;
    background-color: #F4F4F4 !important;
}

.streamlit-expanderHeader p {
    font-size: 22px !important;
    font-weight: 900 !important;
    font-family: 'Courier New', Courier, monospace !important;
    text-transform: uppercase !important;
    letter-spacing: -0.5px !important;
}

[data-testid="stExpanderDetails"] {
    border: 3px solid #000000 !important;
    border-top: none !important;
    box-shadow: 6px 6px 0px 0px #000000 !important;
    background-color: #FFFFFF !important;
    padding: 18px !important;
}

[data-testid="stExpanderDetails"] h1,
[data-testid="stExpanderDetails"] h2,
[data-testid="stExpanderDetails"] h3 {
    font-family: 'Courier New', Courier, monospace !important;
    font-size: 30px !important;
    font-weight: 900 !important;
    text-transform: uppercase !important;
    letter-spacing: -1px !important;
    line-height: 1.15 !important;
    margin-top: 18px !important;
    margin-bottom: 14px !important;
    color: #000000 !important;
}

[data-testid="stExpanderDetails"] p,
[data-testid="stExpanderDetails"] li {
    font-family: 'Courier New', Courier, monospace !important;
    font-size: 18px !important;
    line-height: 1.6 !important;
    color: #000000 !important;
}

[data-testid="stExpanderDetails"] strong {
    font-weight: 900 !important;
    text-transform: uppercase !important;
}

[data-testid="stExpanderDetails"] ul,
[data-testid="stExpanderDetails"] ol {
    padding-left: 24px !important;
    margin-top: 8px !important;
    margin-bottom: 12px !important;
}

/* Slightly smaller on narrow screens */
@media (max-width: 1200px) {
    .neo-title {
        font-size: 42px;
    }
    .neo-section {
        font-size: 28px;
    }
    .neo-metric-value {
        font-size: 34px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 3. HELPERS
# ---------------------------------------------------
def section_header(text):
    st.markdown(f'<div class="neo-section">{text}</div>', unsafe_allow_html=True)

def metric_card(label, value):
    st.markdown(
        f"""
        <div class="neo-metric-card">
            <div class="neo-metric-label">{label}</div>
            <div class="neo-metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def abc_explainer():
    st.markdown(
        """
        <div class="neo-explainer">
            <div class="neo-explainer-title">ABC Segment Guide</div>
            <div class="neo-explainer-text">
                <b>Segment A</b> = highest-value products that drive most of the revenue and need the closest attention.<br>
                <b>Segment B</b> = medium-priority products with steady contribution.<br>
                <b>Segment C</b> = low-value or long-tail products that contribute the least revenue and may need rationalisation.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# 4. DATA PIPELINE
# ---------------------------------------------------
@st.cache_data(ttl=600)
def load_and_verify_data():
    try:
        conn = sqlite3.connect("retail.db")
        df = pd.read_sql("SELECT * FROM enriched_sales", conn)
        conn.close()

        df["date"] = pd.to_datetime(df["date"])

        category_map = {
            "KEGS": "DRAUGHT BEER",
            "STR_SUPPLIES": "STORE SUPPLIES",
            "REF": "REFRIGERATED",
            "DUNNAGE": "SHIPPING MATERIALS"
        }
        df["item_type"] = df["item_type"].replace(category_map)

        if os.path.exists("outputs/product_segments.csv"):
            seg_df = pd.read_csv("outputs/product_segments.csv")[["item_description", "segment"]]
            df = df.merge(seg_df, on="item_description", how="left")
            df["segment"] = df["segment"].fillna("Uncategorized")
        else:
            df["segment"] = "N/A"

        df = df.rename(columns={
            "date": "Transaction Date",
            "total_sales": "Revenue ($)",
            "item_type": "Category",
            "season": "Season",
            "year": "Year",
            "retail_sales": "Retail Revenue",
            "warehouse_sales": "Warehouse Revenue",
            "segment": "ABC Segment",
            "marketing_active": "Marketing Active"
        })

        return df, True, None

    except Exception as e:
        return pd.DataFrame(), False, str(e)

# ---------------------------------------------------
# 5. SIDEBAR & FILTERS
# ---------------------------------------------------
st.sidebar.title("Dashboard Controls")

data, success, error_msg = load_and_verify_data()

if not success:
    st.error(f"Error loading data: {error_msg}")
    st.stop()

years = st.sidebar.multiselect(
    "Select Years",
    sorted(data["Year"].dropna().unique()),
    default=sorted(data["Year"].dropna().unique())
)

seasons = st.sidebar.multiselect(
    "Select Seasons",
    sorted(data["Season"].dropna().unique()),
    default=sorted(data["Season"].dropna().unique())
)

cats = st.sidebar.multiselect(
    "Select Categories",
    sorted(data["Category"].dropna().unique()),
    default=sorted(data["Category"].dropna().unique())[:5]
)

segments = st.sidebar.multiselect(
    "Select Segments",
    sorted(data["ABC Segment"].dropna().unique()),
    default=sorted(data["ABC Segment"].dropna().unique())
)

f_df = data[
    (data["Year"].isin(years)) &
    (data["Season"].isin(seasons)) &
    (data["Category"].isin(cats)) &
    (data["ABC Segment"].isin(segments)) &
    (data["Revenue ($)"] >= 0)
].copy()

# ---------------------------------------------------
# 6. MAIN TITLE
# ---------------------------------------------------
st.markdown('<div class="neo-title">Retail Intelligence Performance</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# 7. KPI ROW
# ---------------------------------------------------
gross_revenue = f_df["Revenue ($)"].sum()
total_transactions = len(f_df)
avg_sale = f_df["Revenue ($)"].mean() if len(f_df) > 0 else 0
warehouse_revenue = f_df["Warehouse Revenue"].sum()

k1, k2, k3, k4 = st.columns(4)

with k1:
    metric_card("Gross Revenue", f"${gross_revenue:,.0f}")
with k2:
    metric_card("Total Transactions", f"{total_transactions:,}")
with k3:
    metric_card("Average Sale Value", f"${avg_sale:,.2f}")
with k4:
    metric_card("Warehouse Revenue", f"${warehouse_revenue:,.0f}")

st.markdown("---")

# ---------------------------------------------------
# 8. EXECUTIVE SUMMARY
# ---------------------------------------------------
section_header("Executive Summary")

def render_enhanced_interpretation(f_df):
    if f_df.empty:
        st.warning("Insufficient data for analysis")
        return

    cat_stats = f_df.groupby("Category")["Revenue ($)"].sum()
    top_cat = cat_stats.idxmax() if not cat_stats.empty else "N/A"

    season_stats = f_df.groupby("Season")["Revenue ($)"].sum()
    peak_season = season_stats.idxmax() if not season_stats.empty else "N/A"

    abc_stats = f_df.groupby("ABC Segment")["Revenue ($)"].sum()
    dom_segment = abc_stats.idxmax() if not abc_stats.empty else "N/A"

    sup_stats = f_df.groupby("supplier")["Revenue ($)"].sum()
    top_sup = sup_stats.idxmax() if not sup_stats.empty else "N/A"

    i_col1, i_col2 = st.columns(2)

    with i_col1:
        st.info(f"""
**Key Performance Indicators**
- Core Revenue Driver: {top_cat}
- Peak Sales Window: {peak_season}
- Top Strategic Supplier: {top_sup}
        """)

    with i_col2:
        st.success(f"""
**Strategic Recommendations**
1. Inventory Priority: Maintain 100% stock for Segment {dom_segment} items.  
2. Marketing Focus: Increase spend for {top_cat} during {peak_season}.  
3. Supplier Relations: Renegotiate terms with {top_sup}.  
        """)

render_enhanced_interpretation(f_df)

st.markdown("---")

# ---------------------------------------------------
# 9. PERFORMANCE VISUALS
# ---------------------------------------------------
section_header("Performance Data Visuals")
abc_explainer()

col_1, col_2 = st.columns(2)

with col_1:
    st.write("**Revenue by Category**")
    cat_data = (
        f_df.groupby("Category")["Revenue ($)"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    if not cat_data.empty:
        st.bar_chart(cat_data, color="#00FFFF")
    else:
        st.warning("No category data")

with col_2:
    st.write("**Revenue by Supplier**")
    sup_data = (
        f_df.groupby("supplier")["Revenue ($)"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    if not sup_data.empty:
        st.bar_chart(sup_data, color="#FFFF00")
    else:
        st.warning("No supplier data")

st.markdown("---")

col_3, col_4 = st.columns([1, 1.2])

with col_3:
    st.write("**Revenue Share by Segment**")
    abc_data = f_df.groupby("ABC Segment")["Revenue ($)"].sum()
    order = ["A", "B", "C"]
    abc_data = abc_data.reindex([o for o in order if o in abc_data.index]).fillna(0)

    if not abc_data.empty and abc_data.sum() > 0:
        fig, ax = plt.subplots(figsize=(4, 4))
        fig.patch.set_facecolor("#FFFFFF")
        ax.set_facecolor("#FFFFFF")

        wedges, texts, autotexts = ax.pie(
            abc_data,
            labels=abc_data.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#FF00FF", "#00FFFF", "#FFFF00"],
            wedgeprops={"width": 0.5, "edgecolor": "#000000", "linewidth": 2},
            textprops={
                "fontsize": 11,
                "fontweight": "bold",
                "family": "monospace",
                "color": "#000000"
            },
            pctdistance=0.75
        )

        ax.axis("equal")

        legend = ax.legend(
            wedges,
            [f"Segment {i}" for i in abc_data.index],
            title="Segments",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
            fontsize=10
        )
        legend.get_frame().set_edgecolor("#000000")
        legend.get_frame().set_linewidth(2)

        st.pyplot(fig)
        plt.close(fig)
    else:
        st.warning("No segment data")

with col_4:
    st.write("**Top Performing Products**")
    if not f_df.empty:
        top_prod_table = (
            f_df.groupby("item_description")["Revenue ($)"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        top_prod_table.columns = ["Product Name", "Total Revenue"]

        top_prod_table["Total Revenue"] = top_prod_table["Total Revenue"].map("${:,.2f}".format)
        st.table(top_prod_table)
    else:
        st.warning("No product data")

st.markdown("---")

# ---------------------------------------------------
# 10. SEASONALITY
# ---------------------------------------------------
section_header("Seasonality Analysis")

if not f_df.empty:
    heat_data = f_df.pivot_table(
        index="Category",
        columns="Season",
        values="Revenue ($)",
        aggfunc="sum"
    ).fillna(0)

    if not heat_data.empty:
        st.write("**Revenue Density Table**")
        styled_heat = heat_data.style.background_gradient(cmap="cool", axis=None).format("${:,.0f}")
        st.table(styled_heat)

        top_season_cat = heat_data.stack().idxmax()
        st.info(f"Insight: Highest revenue density in {top_season_cat[0]} during {top_season_cat[1]}.")
    else:
        st.warning("No seasonality data")
else:
    st.info("Select filters to see data")

st.markdown("---")

# ---------------------------------------------------
# 11. FOOTER
# ---------------------------------------------------
if os.path.exists("outputs/segmentation_insights.md"):
    with st.expander("Full Pipeline Insights"):
        with open("outputs/segmentation_insights.md", "r", encoding="utf-8") as f:
            insights = f.read()
        st.markdown(insights)
else:
    st.info("Pipeline report pending")