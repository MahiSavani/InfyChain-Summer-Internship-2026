"""
Task 5: Interactive Dashboard Creation (Python version of Power BI task)
Dataset: Netflix Titles Data
Author: Mahi Savani (24AIML059)

How to run:
    1. Install requirements:
         pip install streamlit pandas plotly
    2. Keep this file in the SAME folder as netflix_titles.csv
    3. Run:
         streamlit run netflix_dashboard.py
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------------------------------------------
# Page setup
# ----------------------------------------------------------------------
st.set_page_config(page_title="Netflix Dashboard", page_icon="🎬", layout="wide")

# Netflix brand palette
NETFLIX_RED = "#E50914"
NETFLIX_RED_DARK = "#B20710"
NETFLIX_BLACK = "#141414"
NETFLIX_DARKGRAY = "#221F1F"
NETFLIX_LIGHT = "#F5F5F1"

PALETTE = [NETFLIX_RED, "#F5A623", "#B20710", "#831010", "#FF6A5B",
           "#E87A5D", "#D65076", "#8B0000"]

px.defaults.color_discrete_sequence = PALETTE

st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(180deg, {NETFLIX_BLACK} 0%, #0a0a0a 100%);
    }}
    body, p, span, label, li {{
        color: {NETFLIX_LIGHT} !important;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {NETFLIX_DARKGRAY} 0%, {NETFLIX_BLACK} 100%);
        border-right: 3px solid {NETFLIX_RED};
    }}
    section[data-testid="stSidebar"] * {{
        color: {NETFLIX_LIGHT} !important;
    }}
    section[data-testid="stSidebar"] .stMultiSelect [data-baseweb="tag"] {{
        background-color: {NETFLIX_RED} !important;
    }}

    /* Header banner */
    .netflix-header {{
        background: linear-gradient(90deg, {NETFLIX_RED_DARK} 0%, {NETFLIX_RED} 60%, {NETFLIX_BLACK} 100%);
        padding: 24px 32px;
        border-radius: 14px;
        margin-bottom: 22px;
        box-shadow: 0 4px 18px rgba(229,9,20,0.35);
        border: 1px solid #3a0a0d;
    }}
    .netflix-header h1 {{
        color: white;
        font-size: 2.2rem;
        margin: 0;
        font-weight: 900;
        letter-spacing: 0.02em;
        text-shadow: 0 2px 6px rgba(0,0,0,0.5);
    }}
    .netflix-header p {{
        color: #FBD3D3;
        margin: 4px 0 0 0;
        font-size: 0.95rem;
    }}

    /* KPI cards */
    .kpi-card {{
        background: linear-gradient(145deg, {NETFLIX_DARKGRAY} 0%, #1a1717 100%);
        border-radius: 14px;
        padding: 18px 20px;
        border: 1px solid {NETFLIX_RED};
        box-shadow: 0 3px 12px rgba(0,0,0,0.5);
        height: 108px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    .kpi-label {{
        font-size: 0.8rem;
        font-weight: 700;
        color: #C7C7C7;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 4px;
    }}
    .kpi-value {{
        font-size: 1.7rem;
        font-weight: 900;
        color: {NETFLIX_RED};
    }}

    /* Chart containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: {NETFLIX_DARKGRAY};
        border-radius: 14px;
        padding: 6px;
        border: 1px solid #333;
        box-shadow: 0 2px 10px rgba(0,0,0,0.4);
    }}

    h1, h2, h3, h4 {{
        color: {NETFLIX_LIGHT} !important;
    }}

    .stButton>button {{
        background-color: {NETFLIX_RED};
        color: white;
        border-radius: 8px;
        border: none;
        font-weight: 700;
    }}

    .stDataFrame {{
        background-color: {NETFLIX_DARKGRAY};
    }}

    /* Dropdown / multiselect option list (renders in a floating panel) */
    div[data-baseweb="popover"] {{
        background-color: {NETFLIX_DARKGRAY} !important;
    }}
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] li,
    ul[data-baseweb="menu"] {{
        background-color: {NETFLIX_DARKGRAY} !important;
        color: {NETFLIX_LIGHT} !important;
    }}
    li[role="option"] {{
        background-color: {NETFLIX_DARKGRAY} !important;
        color: {NETFLIX_LIGHT} !important;
    }}
    li[role="option"]:hover, li[aria-selected="true"] {{
        background-color: {NETFLIX_RED} !important;
        color: white !important;
    }}
    /* The closed select box itself */
    div[data-baseweb="select"] > div {{
        background-color: {NETFLIX_DARKGRAY} !important;
        color: {NETFLIX_LIGHT} !important;
        border-color: #444 !important;
    }}
    div[data-baseweb="select"] input {{
        color: {NETFLIX_LIGHT} !important;
    }}
    /* Slider value labels */
    div[data-testid="stSlider"] div[data-baseweb="slider"] div {{
        color: {NETFLIX_LIGHT} !important;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="netflix-header">
    <h1>🎬 NETFLIX Content Dashboard</h1>
    <p>Movies &amp; TV Shows Data Analysis &nbsp;•&nbsp; Interactive Streamlit + Plotly dashboard (Python version of Power BI Task 5)</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# Load data
# ----------------------------------------------------------------------
@st.cache_data
def load_netflix():
    df = pd.read_csv("netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    return df

try:
    netflix = load_netflix()
except FileNotFoundError:
    st.error("netflix_titles.csv not found. Place it in the same folder as this script.")
    st.stop()

# ----------------------------------------------------------------------
# Filters (sidebar = Power BI style slicers)
# ----------------------------------------------------------------------
st.sidebar.markdown("### 🔍 Filter Panel")

content_type = st.sidebar.multiselect(
    "Content Type",
    options=sorted(netflix["type"].dropna().unique()),
)

countries = netflix["country"].dropna().str.split(", ").explode().unique()
country_sel = st.sidebar.multiselect(
    "Country",
    options=sorted(countries),
)

rating_sel = st.sidebar.multiselect(
    "Rating",
    options=sorted(netflix["rating"].dropna().unique()),
)

min_year = int(netflix["release_year"].min())
max_year = int(netflix["release_year"].max())
year_range = st.sidebar.slider(
    "Release Year Range", min_year, max_year, (min_year, max_year)
)

# Apply filters
nf_filtered = netflix.copy()
if content_type:
    nf_filtered = nf_filtered[nf_filtered["type"].isin(content_type)]
if country_sel:
    nf_filtered = nf_filtered[
        nf_filtered["country"].fillna("").apply(lambda x: any(c in x for c in country_sel))
    ]
if rating_sel:
    nf_filtered = nf_filtered[nf_filtered["rating"].isin(rating_sel)]
nf_filtered = nf_filtered[
    (nf_filtered["release_year"] >= year_range[0]) & (nf_filtered["release_year"] <= year_range[1])
]

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
    st.markdown(kpi_card("Total Titles", f"{nf_filtered.shape[0]:,}", "🎞️"), unsafe_allow_html=True)
with k2:
    st.markdown(kpi_card("Movies", f"{(nf_filtered['type'] == 'Movie').sum():,}", "🎥"), unsafe_allow_html=True)
with k3:
    st.markdown(kpi_card("TV Shows", f"{(nf_filtered['type'] == 'TV Show').sum():,}", "📺"), unsafe_allow_html=True)
with k4:
    st.markdown(kpi_card("Unique Countries", f"{nf_filtered['country'].dropna().nunique():,}", "🌍"), unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------------------------
# Charts
# ----------------------------------------------------------------------
CHART_LAYOUT = dict(
    font=dict(family="Arial", color=NETFLIX_LIGHT),
    plot_bgcolor=NETFLIX_DARKGRAY,
    paper_bgcolor=NETFLIX_DARKGRAY,
    title_font=dict(size=16, color=NETFLIX_LIGHT),
    legend=dict(font=dict(color=NETFLIX_LIGHT)),
    margin=dict(t=50, l=10, r=10, b=10),
    xaxis=dict(gridcolor="#333", color=NETFLIX_LIGHT),
    yaxis=dict(gridcolor="#333", color=NETFLIX_LIGHT),
)

r1c1, r1c2 = st.columns(2)

with r1c1:
    with st.container(border=True):
        type_counts = nf_filtered["type"].value_counts().reset_index()
        type_counts.columns = ["Type", "Count"]
        fig = px.pie(type_counts, names="Type", values="Count", hole=0.55,
                     title="Movies vs TV Shows", color_discrete_sequence=[NETFLIX_RED, "#F5A623"])
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

with r1c2:
    with st.container(border=True):
        top_countries = (
            nf_filtered["country"].dropna().str.split(", ").explode().value_counts().head(10).reset_index()
        )
        top_countries.columns = ["Country", "Count"]
        fig = px.bar(top_countries, x="Count", y="Country", orientation="h",
                     title="Top 10 Countries by Content Count", color="Count",
                     color_continuous_scale=["#5A0A0A", NETFLIX_RED])
        fig.update_layout(**CHART_LAYOUT)
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig, use_container_width=True)

r2c1, r2c2 = st.columns(2)

with r2c1:
    with st.container(border=True):
        by_year = nf_filtered["year_added"].value_counts().sort_index().reset_index()
        by_year.columns = ["Year Added", "Count"]
        fig = px.area(by_year, x="Year Added", y="Count", markers=True,
                      title="Titles Added to Netflix Over Time")
        fig.update_traces(line_color=NETFLIX_RED, fillcolor="rgba(229,9,20,0.25)")
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

with r2c2:
    with st.container(border=True):
        top_genres = (
            nf_filtered["listed_in"].dropna().str.split(", ").explode().value_counts().head(10).reset_index()
        )
        top_genres.columns = ["Genre", "Count"]
        fig = px.bar(top_genres, x="Genre", y="Count", title="Top 10 Genres", color="Count",
                     color_continuous_scale=["#5A0A0A", NETFLIX_RED])
        fig.update_layout(**CHART_LAYOUT)
        fig.update_xaxes(tickangle=-30)
        st.plotly_chart(fig, use_container_width=True)

r3c1, r3c2 = st.columns(2)

with r3c1:
    with st.container(border=True):
        rating_counts = nf_filtered["rating"].value_counts().head(10).reset_index()
        rating_counts.columns = ["Rating", "Count"]
        fig = px.bar(rating_counts, x="Rating", y="Count", title="Content by Rating", color="Count",
                     color_continuous_scale=["#5A0A0A", NETFLIX_RED])
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

with r3c2:
    with st.container(border=True):
        release_by_year = nf_filtered["release_year"].value_counts().sort_index().reset_index()
        release_by_year.columns = ["Release Year", "Count"]
        fig = px.line(release_by_year, x="Release Year", y="Count", markers=True,
                      title="Content Released by Year")
        fig.update_traces(line_color="#F5A623")
        fig.update_layout(**CHART_LAYOUT)
        st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------------------------------------
# Data table
# ----------------------------------------------------------------------
with st.expander("🔎 View filtered data table"):
    st.dataframe(nf_filtered, use_container_width=True)