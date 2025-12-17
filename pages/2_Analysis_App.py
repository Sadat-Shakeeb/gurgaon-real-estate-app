import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(page_title="Analytics", layout="wide")
st.title("📊 Real Estate Analytics")


# -------------------------------------------------
# Data loading (cached for performance)
# -------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("datasets/data_viz1.csv")
    feature_text = pickle.load(open("datasets/feature_text.pkl", "rb"))
    return df, feature_text


new_df, feature_text = load_data()


# -------------------------------------------------
# 1. Sector-wise Price per Sqft Geo Map
# -------------------------------------------------
st.header("🏙️ Sector-wise Price per Sqft Map")

group_df = (
    new_df
    .groupby("sector", as_index=False)
    .agg({
        "price": "mean",
        "price_per_sqft": "mean",
        "built_up_area": "mean",
        "latitude": "mean",
        "longitude": "mean"
    })
    .set_index("sector")
)

fig_map = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    hover_name=group_df.index,
    height=650
)

st.plotly_chart(fig_map, use_container_width=True)


# -------------------------------------------------
# 2. Features Word Cloud
# -------------------------------------------------
st.header("🛠️ Property Features Word Cloud")

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords={"s"},
    min_font_size=10
).generate(feature_text)

fig_wc, ax_wc = plt.subplots(figsize=(8, 8))
ax_wc.imshow(wordcloud, interpolation="bilinear")
ax_wc.axis("off")

st.pyplot(fig_wc)


# -------------------------------------------------
# 3. Area vs Price Scatter Plot
# -------------------------------------------------
st.header("📐 Area vs Price Analysis")

property_type = st.selectbox("Select Property Type", ["flat", "house"])

filtered_df = new_df[new_df["property_type"] == property_type]

fig_area_price = px.scatter(
    filtered_df,
    x="built_up_area",
    y="price",
    color="bedRoom",
    title=f"Area vs Price ({property_type.capitalize()})",
    labels={
        "built_up_area": "Built-up Area (sq ft)",
        "price": "Price (Cr)"
    }
)

st.plotly_chart(fig_area_price, use_container_width=True)


# -------------------------------------------------
# 4. BHK Distribution Pie Chart
# -------------------------------------------------
st.header("🏠 BHK Distribution")

sector_options = ["overall"] + sorted(new_df["sector"].unique().tolist())
selected_sector = st.selectbox("Select Sector", sector_options)

pie_df = new_df if selected_sector == "overall" else new_df[new_df["sector"] == selected_sector]

fig_bhk_pie = px.pie(
    pie_df,
    names="bedRoom",
    title="BHK Distribution"
)

st.plotly_chart(fig_bhk_pie, use_container_width=True)


# -------------------------------------------------
# 5. BHK Price Comparison (Box Plot)
# -------------------------------------------------
st.header("📦 BHK-wise Price Comparison")

fig_bhk_box = px.box(
    new_df[new_df["bedRoom"] <= 4],
    x="bedRoom",
    y="price",
    title="Price Distribution by BHK",
    labels={
        "bedRoom": "Number of Bedrooms",
        "price": "Price (Cr)"
    }
)

st.plotly_chart(fig_bhk_box, use_container_width=True)


# -------------------------------------------------
# 6. Price Distribution by Property Type
# -------------------------------------------------
st.header("📊 Price Distribution: Flat vs House")

fig_dist, ax_dist = plt.subplots(figsize=(10, 4))

sns.kdeplot(
    new_df[new_df["property_type"] == "house"]["price"],
    label="House",
    ax=ax_dist
)
sns.kdeplot(
    new_df[new_df["property_type"] == "flat"]["price"],
    label="Flat",
    ax=ax_dist
)

ax_dist.set_title("Price Distribution by Property Type")
ax_dist.set_xlabel("Price (Cr)")
ax_dist.legend()

st.pyplot(fig_dist)
