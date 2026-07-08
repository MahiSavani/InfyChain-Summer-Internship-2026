import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(page_title="BlinkIT Dashboard", page_icon="🛒", layout="wide")

# Blinkit brand palette
BLINKIT_YELLOW = "#F8CB46"
BLINKIT_YELLOW_DARK = "#E8A100"
BLINKIT_GREEN = "#0C831F"
BLINKIT_GREEN_LIGHT = "#3EA847"
BLINKIT_DARK = "#1A1A1A"
BLINKIT_CREAM = "#FFF8E7"

PALETTE = [BLINKIT_GREEN, BLINKIT_YELLOW_DARK, BLINKIT_GREEN_LIGHT, "#F6B93B",
           "#2E7D32", "#FFD166", "#43A047", "#FFC93C"]

px.defaults.color_discrete_sequence = PALETTE
px.defaults.template = "plotly_white"

st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(180deg, {BLINKIT_CREAM} 0%, #FFFFFF 30%);
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {BLINKIT_YELLOW} 0%, {BLINKIT_YELLOW_DARK} 100%);
        border-right: 4px solid {BLINKIT_GREEN};
    }}
    section[data-testid="stSidebar"] * {{
        color: {BLINKIT_DARK} !important;
    }}
    section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {{
        background-color: {BLINKIT_GREEN} !important;
    }}
    section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] span {{
        color: white !important;
    }}

    /* Header banner */
    .blinkit-header {{
        background: linear-gradient(90deg, {BLINKIT_GREEN} 0%, {BLINKIT_GREEN_LIGHT} 100%);
        padding: 22px 32px;
        border-radius: 16px;
        margin-bottom: 22px;
        box-shadow: 0 4px 14px rgba(12,131,31,0.25);
    }}
    .blinkit-header h1 {{
        color: {BLINKIT_YELLOW};
        font-size: 2.1rem;
        margin: 0;
        font-weight: 800;
    }}
    .blinkit-header p {{
        color: #EAFCE9;
        margin: 4px 0 0 0;
        font-size: 0.95rem;
    }}

    /* KPI cards */
    .kpi-card {{
        background-color: {BLINKIT_YELLOW};
        border-radius: 14px;
        padding: 18px 20px;
        border: 2px solid {BLINKIT_YELLOW_DARK};
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        height: 108px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .kpi-label {{
        font-size: 0.82rem;
        font-weight: 700;
        color: {BLINKIT_DARK};
        text-transform: uppercase;
        letter-spacing: 0.03em;
        margin-bottom: 4px;
    }}
    .kpi-value {{
        font-size: 1.65rem;
        font-weight: 800;
        color: {BLINKIT_GREEN};
    }}

    /* Chart containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: white;
        border-radius: 14px;
        padding: 6px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}

    h1, h2, h3 {{
        color: {BLINKIT_DARK};
    }}

    .stButton>button {{
        background-color: {BLINKIT_GREEN};
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: 700;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="blinkit-header">
    <h1>🛒 Blinkit Grocery Sales Dashboard</h1>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Load data
# ----------------------------------------------------------------------
@st.cache_data
def load_blinkit():
    return pd.read_csv("blinkit_data.csv")

try:
    blinkit = load_blinkit()
except FileNotFoundError:
    st.error("blinkit_data.csv not found. Place it in the same folder as this script.")
    st.stop()

# ----------------------------------------------------------------------
# Filters (sidebar = Power BI style slicers)
# ----------------------------------------------------------------------
st.sidebar.markdown("### 🔍 Filter Panel")

outlet_type = st.sidebar.multiselect(
    "Outlet Type",
    options=sorted(blinkit["Outlet Type"].dropna().unique()),
)
outlet_size = st.sidebar.multiselect(
    "Outlet Size",
    options=sorted(blinkit["Outlet Size"].dropna().unique()),
)
location_type = st.sidebar.multiselect(
    "Outlet Location Type",
    options=sorted(blinkit["Outlet Location Type"].dropna().unique()),
)
item_type = st.sidebar.multiselect(
    "Item Type",
    options=sorted(blinkit["Item Type"].dropna().unique()),
)
fat_content = st.sidebar.radio(
    "Item Fat Content",
    options=["All"] + sorted(blinkit["Item Fat Content"].dropna().unique().tolist()),
)

# Apply filters
filtered = blinkit.copy()
if outlet_type:
    filtered = filtered[filtered["Outlet Type"].isin(outlet_type)]
if outlet_size:
    filtered = filtered[filtered["Outlet Size"].isin(outlet_size)]
if location_type:
    filtered = filtered[filtered["Outlet Location Type"].isin(location_type)]
if item_type:
    filtered = filtered[filtered["Item Type"].isin(item_type)]
if fat_content != "All":
    filtered = filtered[filtered["Item Fat Content"] == fat_content]

# ----------------------------------------------------------------------
# KPI cards
# ----------------------------------------------------------------------
def kpi_card(label, value, icon):
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{icon} {label}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(kpi_card("Total Sales", f"${filtered['Sales'].sum():,.0f}", "💰"), unsafe_allow_html=True)
with k2:
    st.markdown(kpi_card("Avg Sales / Item", f"${filtered['Sales'].mean():,.2f}", "📈"), unsafe_allow_html=True)
with k3:
    st.markdown(kpi_card("No. of Items", f"{filtered.shape[0]:,}", "📦"), unsafe_allow_html=True)
with k4:
    st.markdown(kpi_card("Avg Rating", f"{filtered['Rating'].mean():,.2f} ★", "⭐"), unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------------------------
# Charts
# ----------------------------------------------------------------------
CHART_LAYOUT = dict(
    font=dict(family="Arial", color=BLINKIT_DARK),
    plot_bgcolor="white",
    paper_bgcolor="white",
    title_font=dict(size=16, color=BLINKIT_DARK),
    margin=dict(t=50, l=10, r=10, b=10),
)

r1c1, r1c2 = st.columns(2)

with r1c1:
    with st.container(border=True):
        sales_by_outlet = (
            filtered.groupby("Outlet Type")["Sales"].sum().reset_index().sort_values("Sales", ascending=False)
        )
        fig = px.bar(sales_by_outlet, x="Outlet Type", y="Sales", title="Total Sales by Outlet Type",
                     color="Outlet Type", text_auto=".2s", color_discrete_sequence=PALETTE)
        fig.update_layout(**CHART_LAYOUT, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

with r1c2:
    with st.container(border=True):
        sales_by_item = (
            filtered.groupby("Item Type")["Sales"].sum().reset_index().sort_values("Sales", ascending=False).head(10)
        )
        fig = px.bar(sales_by_item, x="Sales", y="Item Type", orientation="h",
                     title="Top 10 Item Types by Sales", color="Sales",
                     color_continuous_scale=[BLINKIT_YELLOW, BLINKIT_GREEN])
        fig.update_layout(yaxis={"categoryorder": "total ascending"}, **CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

r2c1, r2c2 = st.columns(2)

with r2c1:
    with st.container(border=True):
        sales_by_year = (
            filtered.groupby("Outlet Establishment Year")["Sales"].sum().reset_index().sort_values("Outlet Establishment Year")
        )
        fig = px.area(sales_by_year, x="Outlet Establishment Year", y="Sales", markers=True,
                      title="Sales Trend by Outlet Establishment Year")
        fig.update_traces(line_color=BLINKIT_GREEN, fillcolor="rgba(248,203,70,0.45)")
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

with r2c2:
    with st.container(border=True):
        fat_pie = filtered["Item Fat Content"].value_counts().reset_index()
        fat_pie.columns = ["Item Fat Content", "Count"]
        fig = px.pie(fat_pie, names="Item Fat Content", values="Count", hole=0.55,
                     title="Item Fat Content Share", color_discrete_sequence=[BLINKIT_GREEN, BLINKIT_YELLOW])
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

r3c1, r3c2 = st.columns(2)

with r3c1:
    with st.container(border=True):
        sales_by_location = (
            filtered.groupby("Outlet Location Type")["Sales"].sum().reset_index().sort_values("Sales", ascending=False)
        )
        fig = px.bar(sales_by_location, x="Outlet Location Type", y="Sales",
                     title="Sales by Outlet Location Type", color="Outlet Location Type",
                     color_discrete_sequence=PALETTE)
        fig.update_layout(**CHART_LAYOUT, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

with r3c2:
    with st.container(border=True):
        rating_dist = filtered["Rating"].value_counts().sort_index().reset_index()
        rating_dist.columns = ["Rating", "Count"]
        fig = px.bar(rating_dist, x="Rating", y="Count", title="Rating Distribution", color="Rating",
                     color_continuous_scale=[BLINKIT_YELLOW, BLINKIT_GREEN])
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------------------
# Data table
# ----------------------------------------------------------------------
with st.expander("🔎 View filtered data table"):
    st.dataframe(filtered, use_container_width=True)
