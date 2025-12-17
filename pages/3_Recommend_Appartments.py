import streamlit as st
import pickle
import pandas as pd
import numpy as np

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(page_title="Apartment Recommendations", layout="wide")

st.title("🏢 Apartment Recommendation System")
st.write(
    """
    This page helps you **discover suitable apartments in Gurgaon** in two ways:

    1️⃣ **Location-based search** – Find apartments within a selected distance from a landmark  
    2️⃣ **Similarity-based recommendation** – Get apartments similar to a selected property based on features  
    """
)

# -------------------------------------------------
# Load Data
# -------------------------------------------------
@st.cache_resource
def load_recommendation_data():
    location_df = pickle.load(open("datasets/location_distance.pkl", "rb"))
    cosine_sim1 = pickle.load(open("datasets/cosine_sim1.pkl", "rb"))
    cosine_sim2 = pickle.load(open("datasets/cosine_sim2.pkl", "rb"))
    cosine_sim3 = pickle.load(open("datasets/cosine_sim3.pkl", "rb"))
    return location_df, cosine_sim1, cosine_sim2, cosine_sim3

location_df, cosine_sim1, cosine_sim2, cosine_sim3 = load_recommendation_data()


# -------------------------------------------------
# Recommendation Function
# -------------------------------------------------
def recommend_properties_with_scores(property_name, top_n=5):
    """
    Recommends similar properties using a weighted cosine similarity
    computed from textual features such as:
    - Property Name
    - Location Advantages
    - Price Details
    - Top Facilities
    """
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1.0 * cosine_sim3

    sim_scores = list(
        enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)])
    )

    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1: top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1: top_n + 1]]

    return pd.DataFrame(
        {
            "Recommended Property": location_df.index[top_indices],
            "Similarity Score": np.round(top_scores, 3),
        }
    )


# -------------------------------------------------
# SECTION 1: Location-Based Apartment Search
# -------------------------------------------------
st.divider()
st.header("📍 Find Apartments Near a Landmark")

st.write(
    """
    **How this works:**
    - Select a **popular landmark in Gurgaon**
    - Choose a **radius (in kilometers)**
    - The system will list apartments located **within that distance**
    """
)

col1, col2 = st.columns(2)

with col1:
    selected_location = st.selectbox(
        "Select Landmark", sorted(location_df.columns.to_list())
    )

with col2:
    radius = st.number_input("Radius (in KM)", min_value=1.0, step=0.5)

if st.button("🔍 Search Nearby Apartments"):
    result_ser = (
        location_df[location_df[selected_location] < radius * 1000][
            selected_location
        ]
        .sort_values()
    )

    if result_ser.empty:
        st.warning("No apartments found within the selected radius.")
    else:
        st.success(f"Apartments within {radius} km of {selected_location}:")
        for property_name, distance in result_ser.items():
            st.write(f"• **{property_name}** — {round(distance / 1000, 2)} km")

# -------------------------------------------------
# SECTION 2: Similar Apartment Recommendation
# -------------------------------------------------
st.divider()
st.header("🤝 Find Similar Apartments")

st.write(
    """
    **How this works:**
    - Select an apartment you like
    - The system analyzes **textual features** such as:
      - Location advantages
      - Facilities
      - Pricing details
    - It then recommends **similar apartments** using **TF-IDF + cosine similarity**
    """
)

selected_apartment = st.selectbox(
    "Select an Apartment", sorted(location_df.index.to_list())
)

if st.button("✨ Recommend Similar Apartments"):
    recommendation_df = recommend_properties_with_scores(selected_apartment)

    st.success("Top similar apartment recommendations:")
    st.dataframe(recommendation_df, use_container_width=True)

# -------------------------------------------------
# Footer Explanation
# -------------------------------------------------
st.divider()
st.caption(
    """
    📌 **Note:**  
    Similarity scores are computed using a weighted combination of multiple feature representations.
    Higher scores indicate greater similarity in amenities, pricing context, and location advantages.
    """
)
