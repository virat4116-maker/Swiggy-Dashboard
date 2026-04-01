import streamlit as st
import pandas as pd

st.set_page_config(page_title="Swiggy Dashboard", layout="wide")

df = pd.read_csv("data/swiggy_clean.csv")

# 👉 SIDEBAR FILTER
st.sidebar.header("Filters")

city = st.sidebar.selectbox("Select City", df['restaurant_city'].unique())

filtered_df = df[df['restaurant_city'] == city]

# 👉 TITLE
st.title("🍔 Swiggy Sales Analytics Dashboard")

# 👉 KPI
col1, col2, col3 = st.columns(3)

col1.metric("Total Orders", len(filtered_df))
col2.metric("Total Revenue", f"₹ {filtered_df['total_amount'].sum():,.0f}")
col3.metric("Avg Rating", round(filtered_df['order_rating'].mean(), 2))

st.divider()

# 👉 CHARTS
st.subheader(f"Orders in {city}")
st.bar_chart(filtered_df['cuisine_type'].value_counts())

st.subheader("Revenue Trend")
st.line_chart(filtered_df.groupby('order_date')['total_amount'].sum())