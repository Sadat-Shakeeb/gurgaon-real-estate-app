import streamlit as st
import pickle
import pandas as pd
import numpy as np

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="Property Price Predictor", layout="wide")

st.title("🏠 Property Price Prediction")
st.write(
    """
    This tool estimates the **market price of a residential property in Gurgaon**  
    based on property characteristics, location, and amenities.

    👉 Fill in the details below and click **Predict Price** to get an estimated range.
    """
)

# -------------------------------------------------
# Load Data & Model
# -------------------------------------------------
@st.cache_resource
def load_prediction_assets():
    with open("df.pkl", "rb") as f:
        df = pickle.load(f)
    with open("pipeline.pkl", "rb") as f:
        pipeline = pickle.load(f)
    return df, pipeline

df, pipeline = load_prediction_assets()


# -------------------------------------------------
# Input Section
# -------------------------------------------------
st.divider()
st.header("📋 Property Details")

st.write(
    """
    Please provide the property details as accurately as possible.
    All inputs are based on real listings used to train the model.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    property_type = st.selectbox(
        "Property Type",
        ["flat", "house"],
        help="Select whether the property is a flat or an independent house"
    )

    sector = st.selectbox(
        "Sector",
        sorted(df["sector"].unique().tolist()),
        help="Sector or locality where the property is located"
    )

    bedrooms = float(
        st.selectbox(
            "Number of Bedrooms (BHK)",
            sorted(df["bedRoom"].unique().tolist())
        )
    )

with col2:
    bathroom = float(
        st.selectbox(
            "Number of Bathrooms",
            sorted(df["bathroom"].unique().tolist())
        )
    )

    balcony = st.selectbox(
        "Number of Balconies",
        sorted(df["balcony"].unique().tolist())
    )

    property_age = st.selectbox(
        "Property Age / Possession",
        sorted(df["agePossession"].unique().tolist()),
        help="Age or possession category of the property"
    )

with col3:
    built_up_area = float(
        st.number_input(
            "Built-up Area (sq ft)",
            min_value=300,
            step=50,
            help="Total built-up area of the property"
        )
    )

    servant_room = float(
        st.selectbox("Servant Room", [0.0, 1.0], format_func=lambda x: "Yes" if x == 1 else "No")
    )

    store_room = float(
        st.selectbox("Store Room", [0.0, 1.0], format_func=lambda x: "Yes" if x == 1 else "No")
    )

st.divider()
st.header("✨ Furnishing & Luxury Details")

col4, col5, col6 = st.columns(3)

with col4:
    furnishing_type = st.selectbox(
        "Furnishing Type",
        sorted(df["furnishing_type"].unique().tolist())
    )

with col5:
    luxury_category = st.selectbox(
        "Luxury Category",
        sorted(df["luxury_category"].unique().tolist()),
        help="Indicates the level of luxury based on amenities and finish"
    )

with col6:
    floor_category = st.selectbox(
        "Floor Category",
        sorted(df["floor_category"].unique().tolist()),
        help="Floor level classification of the property"
    )

# -------------------------------------------------
# Prediction Section
# -------------------------------------------------
st.divider()
st.header("📈 Price Estimation")

if st.button("🔮 Predict Price"):
    # Prepare input DataFrame
    input_data = [[
        property_type, sector, bedrooms, bathroom, balcony,
        property_age, built_up_area, servant_room, store_room,
        furnishing_type, luxury_category, floor_category
    ]]

    columns = [
        "property_type", "sector", "bedRoom", "bathroom", "balcony",
        "agePossession", "built_up_area", "servant room", "store room",
        "furnishing_type", "luxury_category", "floor_category"
    ]

    input_df = pd.DataFrame(input_data, columns=columns)

    # Prediction
    base_price = np.expm1(pipeline.predict(input_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Display Results
    st.success("🏠 Estimated Property Price Range")

    colA, colB, colC = st.columns(3)

    colA.metric("Minimum Price", f"₹ {low:.2f} Cr")
    colB.metric("Expected Price", f"₹ {base_price:.2f} Cr")
    colC.metric("Maximum Price", f"₹ {high:.2f} Cr")

    st.caption(
        "📌 The price range is an estimate based on historical data and selected features."
    )
