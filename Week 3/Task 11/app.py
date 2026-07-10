"""
app.py
Task 9 - End-to-End Data Science Project (Deployment)
A polished Streamlit web app: user enters key house details -> model predicts SalePrice.

Run with:
    streamlit run app.py
"""

import pickle
import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# Page setup (must be first Streamlit command)
# ---------------------------------------------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Custom styling
# ---------------------------------------------------------
st.markdown("""
<style>
    .main { background-color: #f7f9fb; }

    .hero {
        background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
        padding: 2.2rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 { margin: 0; font-size: 2.1rem; }
    .hero p { margin: 0.4rem 0 0 0; opacity: 0.92; font-size: 1rem; }

    div[data-testid="stMetric"] {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1rem 1rem 0.6rem 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    .result-card {
        background: white;
        border-radius: 16px;
        padding: 1.8rem 2rem;
        text-align: center;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    }
    .result-card .label {
        color: #6b7280;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    .result-card .price {
        color: #0f766e;
        font-size: 3rem;
        font-weight: 800;
        margin: 0.3rem 0;
    }

    .stButton>button {
        background: #0f766e;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        border: none;
    }
    .stButton>button:hover { background: #0d5f58; color: white; }

    section[data-testid="stSidebar"] { background-color: #ffffff; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Load trained model + supporting artifacts
# ---------------------------------------------------------
@st.cache_resource
def load_artifacts():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    with open('feature_defaults.pkl', 'rb') as f:
        feature_defaults = pickle.load(f)
    with open('feature_columns.pkl', 'rb') as f:
        feature_columns = pickle.load(f)
    return model, encoders, feature_defaults, feature_columns

model, encoders, feature_defaults, feature_columns = load_artifacts()

# ---------------------------------------------------------
# Hero header
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🏠 House Price Predictor</h1>
    <p>Task 9 · End-to-End Data Science Project &nbsp;|&nbsp; Random Forest model trained on the Ames Housing dataset (Task 8)</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar — user inputs
# ---------------------------------------------------------
with st.sidebar:
    st.header("🏗️ House Details")
    st.caption("Fill in the key features below")

    st.subheader("Size & Quality")
    overall_qual = st.slider("Overall Quality", 1, 10, 6, help="1 = Poor, 10 = Excellent")
    gr_liv_area = st.number_input("Living Area (sq ft)", 300, 6000, 1500, step=50)
    total_bsmt_sf = st.number_input("Basement Area (sq ft)", 0, 6000, 800, step=50)
    lot_area = st.number_input("Lot Area (sq ft)", 500, 220000, 9000, step=100)

    st.subheader("Rooms & Garage")
    tot_rms_abv_grd = st.slider("Total Rooms Above Grade", 2, 15, 6)
    full_bath = st.slider("Full Bathrooms", 0, 4, 2)
    garage_cars = st.slider("Garage Capacity (cars)", 0, 5, 2)

    st.subheader("Age")
    year_built = st.number_input("Year Built", 1870, 2026, 2005, step=1)
    year_remod = st.number_input("Year Remodeled", 1870, 2026, 2005, step=1)

    st.subheader("Quality Ratings")
    kitchen_qual = st.selectbox("Kitchen Quality", ["Ex", "Gd", "TA", "Fa", "Po"], index=2)
    exter_qual = st.selectbox("Exterior Quality", ["Ex", "Gd", "TA", "Fa", "Po"], index=2)
    neighborhood = st.selectbox(
        "Neighborhood",
        sorted(list(encoders['Neighborhood'].classes_)) if 'Neighborhood' in encoders else ["NAmes"],
    )

    st.markdown("---")
    predict_btn = st.button("🔮 Predict Sale Price", use_container_width=True)

# ---------------------------------------------------------
# Build full feature row (user inputs + defaults for the rest)
# ---------------------------------------------------------
def build_input_row():
    row = feature_defaults.copy()  # start with medians/modes for ALL features

    row['OverallQual'] = overall_qual
    row['GrLivArea'] = gr_liv_area
    row['TotalBsmtSF'] = total_bsmt_sf
    row['GarageCars'] = garage_cars
    row['FullBath'] = full_bath
    row['YearBuilt'] = year_built
    row['TotRmsAbvGrd'] = tot_rms_abv_grd
    row['LotArea'] = lot_area
    row['YearRemodAdd'] = year_remod

    if 'KitchenQual' in encoders:
        row['KitchenQual'] = int(encoders['KitchenQual'].transform([kitchen_qual])[0])
    if 'ExterQual' in encoders:
        row['ExterQual'] = int(encoders['ExterQual'].transform([exter_qual])[0])
    if 'Neighborhood' in encoders:
        row['Neighborhood'] = int(encoders['Neighborhood'].transform([neighborhood])[0])

    input_df = pd.DataFrame([row])[feature_columns]
    return input_df

# ---------------------------------------------------------
# Main area
# ---------------------------------------------------------
left, right = st.columns([1.3, 1])

with left:
    st.subheader("📋 Summary of Your Inputs")
    c1, c2, c3 = st.columns(3)
    c1.metric("Overall Quality", f"{overall_qual}/10")
    c2.metric("Living Area", f"{gr_liv_area:,} sqft")
    c3.metric("Garage", f"{garage_cars} car(s)")

    c4, c5, c6 = st.columns(3)
    c4.metric("Bathrooms", full_bath)
    c5.metric("Total Rooms", tot_rms_abv_grd)
    c6.metric("Year Built", year_built)

    st.info(f"📍 Neighborhood: **{neighborhood}**  ·  Kitchen: **{kitchen_qual}**  ·  Exterior: **{exter_qual}**")

with right:
    st.subheader("💰 Prediction")
    if predict_btn:
        input_df = build_input_row()
        prediction = model.predict(input_df)[0]

        st.markdown(f"""
        <div class="result-card">
            <div class="label">Estimated Sale Price</div>
            <div class="price">${prediction:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("See all feature values sent to the model"):
            st.dataframe(input_df.T.rename(columns={0: "Value"}), use_container_width=True)
    else:
        st.markdown("""
        <div class="result-card">
            <div class="label">Waiting for input</div>
            <div style="color:#9ca3af; font-size:1.2rem; margin-top:0.5rem;">
                👈 Fill in the house details and click<br><b>Predict Sale Price</b>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption(
    "Model: Random Forest Regressor · Trained on the Kaggle Ames House Price dataset · "
    "Task 8/9 · InfyChain Data Science Internship"
)