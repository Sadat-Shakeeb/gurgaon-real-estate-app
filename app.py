import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate App",
    page_icon="🏠",
    layout="wide"
)

# -------------------------------------------------
# Main Title
# -------------------------------------------------
st.title("🏠 Gurgaon Real Estate Explorer")

st.write(
    """
    Welcome to the **Gurgaon Real Estate Explorer**.  
    This application helps you **understand property prices**, **explore market trends**,  
    and **discover suitable apartments** in Gurgaon — all in one place.
    """
)

st.divider()

# -------------------------------------------------
# What You Can Do Section
# -------------------------------------------------
st.header("✨ What You Can Do Here")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💰 Price Prediction")
    st.write(
        """
        Estimate the price of a property by entering details such as:
        - Property type
        - Location (sector)
        - Size and configuration
        - Furnishing and amenities

        This helps you get a **realistic price range** before making decisions.
        """
    )

with col2:
    st.subheader("📊 Market Analysis")
    st.write(
        """
        Explore interactive visualizations to:
        - Compare prices across sectors
        - Understand how size impacts price
        - See BHK distributions
        - Compare flats vs houses

        Ideal for **market understanding and research**.
        """
    )

with col3:
    st.subheader("🏢 Apartment Recommendations")
    st.write(
        """
        Discover apartments using two simple approaches:
        - Find properties near a landmark within a chosen distance
        - Get recommendations similar to a selected apartment

        Helps you **shortlist properties quickly**.
        """
    )

st.divider()

# -------------------------------------------------
# How to Navigate
# -------------------------------------------------
st.header("🧭 How to Get Started")

st.write(
    """
    Use the **sidebar on the left** to navigate between sections:

    - **Price Prediction** → Estimate property prices  
    - **Analytics** → Explore market insights  
    - **Recommend Apartments** → Discover and compare properties  

    👉 Start with **Price Prediction** if you want a quick estimate,  
    or explore **Analytics** if you want a deeper market understanding.
    """
)

# -------------------------------------------------
# Sidebar Helper
# -------------------------------------------------
st.sidebar.success("⬅️ Select a section to begin")
