import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data  # Cache the data to improve performance
def load_data():
    return pd.read_csv('data/sales_data.csv')

df = load_data()

# Calculate total revenue
total_revenue = df['quantity'].mul(df['price']).sum()

# Streamlit app
st.title("Sales Data Dashboard")
st.write("### Total Revenue")
st.write(f"${total_revenue:,.2f}")

st.write("### Revenue by Product")
product_revenue = df.groupby('product').apply(lambda x: (x['quantity'] * x['price']).sum())
st.bar_chart(product_revenue)

st.write("### Monthly Sales Trends")
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M').astype(str)
monthly_revenue = df.groupby('month').apply(lambda x: (x['quantity'] * x['price']).sum())
st.line_chart(monthly_revenue)

st.write("### Top 5 Customers by Spending")
top_customers = df.groupby('customer_id').apply(lambda x: (x['quantity'] * x['price']).sum()).nlargest(5)
st.bar_chart(top_customers)