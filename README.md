# 🏠 Gurgaon Real Estate Data Science Application

🔗 **Live App:** https://gurgaon-real-estate-app.streamlit.app  

---

## 📌 Capstone Project Overview

This capstone project focuses on applying **data science and machine learning techniques** to solve real-world problems in the **real estate domain**.  
The application provides:

- 📈 **Property price prediction**
- 📊 **Interactive market analytics**
- 🏘️ **Apartment recommendation system**

The project covers the **complete end-to-end data science lifecycle** — from data collection and preprocessing to model building, evaluation, and deployment using **Streamlit Cloud**.

---
```
## 🗂️ Project Structure

Real-Estate-App/
│
├── app.py                     # Main entry point (Home Page)
│
├── pages/
│   ├── 1_Price_Predictor.py   # Price prediction module
│   ├── 2_Analytics.py         # Market analytics & visualizations
│   └── 3_Recommend_Appartments.py  # Recommendation system
│
├── datasets/
│   ├── data_viz1.csv
│   ├── feature_text.pkl
│   ├── location_distance.pkl
│   ├── cosine_sim1.pkl
│   ├── cosine_sim2.pkl
│   └── cosine_sim3.pkl
│
├── df.pkl                     # Processed dataset
├── pipeline.pkl               # Trained ML pipeline
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

```
---
## 🎥 Application Demo (Silent Walkthrough)

A short screen-recorded walkthrough demonstrating the core features of the application, Download and watch a short screen-recorded demo of the application. 

👉 [View Demo Video](https://github.com/Sadat-Shakeeb/gurgaon-real-estate-app/releases/tag/v1.0)

---
---

## 📥 Data Collection

- Real estate data was **self-scraped from the 99acres website**.
- Additional datasets from similar property listing platforms were explored.
- The focus city for this project is **Gurgaon**.

---

## 🧹 Data Cleaning & Merging

- Missing values were handled carefully to maintain data integrity.
- Inconsistent formats were standardized.
- Data from **houses and flats** was merged into a unified dataset.

---

## 🛠️ Feature Engineering

Several meaningful features were engineered to enrich the dataset:

- Room indicators (servant room, store room)
- Built-up area with type specifications
- Age of possession
- Furnishing type
- Luxury category score
- Floor category

These features helped improve both **model performance** and **interpretability**.

---

## 🔍 Exploratory Data Analysis (EDA)

- Univariate and multivariate analyses were conducted.
- Pandas profiling was used to understand data distribution and structure.
- Key relationships between **location, area, BHK, and price** were identified.

---

## 🚨 Outlier Handling & Missing Value Imputation

- Outliers were detected and removed to improve robustness.
- Missing values in critical columns (area, bedrooms, etc.) were imputed using appropriate strategies.

---

## 🎯 Feature Selection

Multiple feature selection techniques were applied:

- Correlation analysis
- Random Forest & Gradient Boosting feature importance
- Permutation importance
- LASSO regression
- Recursive Feature Elimination (RFE)
- SHAP (Explainable AI)

This ensured that only the most impactful features were used for modeling.

---

## 🤖 Model Selection & Evaluation

### Baseline Model
- Cross-validation score: **0.8845**
- Mean Absolute Error: **0.5324**

### Models Evaluated
- Linear Regression  
- Support Vector Regression (SVR)  
- Random Forest Regressor  
- Decision Tree Regressor  
- K-Nearest Neighbors Regressor  
- Ridge Regression  
- LASSO Regression  
- ElasticNet Regression  
- Multi-layer Perceptron (MLP)  
- Gradient Boosting Regressor  
- **XGBoost Regressor**

### Final Model
- **XGBoost Regressor**
- Achieved **~0.91 R² score** after hyperparameter tuning
- Selected for its superior performance and generalization ability

---

## 🌐 Streamlit Web Application

The trained model and analytics were deployed using **Streamlit**, providing an intuitive user interface with three main sections.

---

## 🔮 1. Price Prediction Module

Users can estimate property prices by selecting:

- Property type (Flat / House)
- Sector
- Bedrooms & Bathrooms
- Balconies
- Property age
- Built-up area
- Servant room & Store room
- Furnishing type
- Luxury category
- Floor category

📌 The model predicts:
- Expected price
- Minimum & maximum estimated price range

---

## 📊 2. Analytics Module

This section provides visual insights into the Gurgaon real estate market.

### Visualizations Included:

1. **Sector-wise Price per Sqft Geo Map**
   - Bubble size represents built-up area
   - Color indicates price per sqft
   - Highlights location-based price variation

2. **Amenities Word Cloud**
   - Shows frequently available property features
   - Highlights standard vs luxury amenities

3. **Area vs Price Scatter Plot**
   - Separate views for flats and houses
   - Shows price trends across different sizes and BHKs

4. **BHK Distribution Pie Chart**
   - Overall and sector-wise BHK distribution
   - Interactive sector selection

5. **BHK-wise Price Comparison (Box Plot)**
   - Shows price spread and outliers for each BHK category

6. **Price Distribution by Property Type**
   - Side-by-side comparison of flats vs houses

---

## 📊 Insights & Observations

### Key Takeaways:
- Location plays a stronger role in pricing than size alone.
- Most listings cater to mid-range buyers; luxury features act as differentiators.
- Houses show higher price variability than flats.
- Premium flats in prime locations can match house prices.
- Higher BHKs exhibit greater price dispersion.

---

## 🏘️ 3. Apartment Recommendation System

The recommendation engine is built using:

- **TF-IDF Vectorization**
- **Cosine Similarity**

### Features Used:
- Property Name
- Location Advantages
- Price Details
- Top Facilities

### User Capabilities:
- Search properties near a selected Gurgaon landmark within a given radius
- Get similar apartment recommendations based on a selected property

This helps users discover **nearby and comparable properties** efficiently.

---

## ☁️ Deployment

- The complete application is deployed on **Streamlit Community Cloud**
- Fully accessible via a web browser
- No local setup required for users

🔗 **Live App:** https://gurgaon-real-estate-app.streamlit.app

---

## ✅ Conclusion

This project demonstrates:
- Strong understanding of **data science fundamentals**
- Practical application of **machine learning models**
- Effective use of **visual analytics**
- Deployment of a **real-world, user-facing application**

It showcases an end-to-end workflow from raw data to a fully deployed analytics and prediction platform.

---

## 👤 Author
**Sadat Shakeeb**
