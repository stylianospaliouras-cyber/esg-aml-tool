import streamlit as st
import requests
import pandas as pd

st.title("🌍 ESG & AML Tool")

API_URL = "http://127.0.0.1:8000/entities"  # FastAPI endpoint

# Fetch data from FastAPI
try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    st.error(f"Error fetching data: {e}")
    data = []

# Convert to DataFrame
if data:
    df = pd.DataFrame(data)

    # Sidebar filters
    st.sidebar.header("🔎 Filters")

    countries = ["All"] + sorted(df["country"].dropna().unique().tolist())
    risks = ["All"] + sorted(df["risk"].dropna().unique().tolist())

    country_filter = st.sidebar.selectbox("Select Country", countries)
    risk_filter = st.sidebar.selectbox("Select Risk Level", risks)

    # Apply filters
    filtered_df = df.copy()
    if country_filter != "All":
        filtered_df = filtered_df[filtered_df["country"] == country_filter]
    if risk_filter != "All":
        filtered_df = filtered_df[filtered_df["risk"] == risk_filter]

    # Show results
    st.subheader("📊 Entities Table")
    st.dataframe(filtered_df)
else:
    st.warning("No data available. Please check your backend or Supabase.")


