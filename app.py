import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
@st.cache_data  # Cache the data to improve performance
def load_data():
    return pd.read_csv('data/sales_data.csv')

df = load_data()
df['order_date'] = pd.to_datetime(df['order_date'])

# Sidebar for filters
st.sidebar.title("Filters")

# Date range filter
min_date = df['order_date'].min()
max_date = df['order_date'].max()
start_date, end_date = st.sidebar.date_input("Select Date Range", [min_date, max_date])

# Product filter
products = df['product'].unique()
selected_products = st.sidebar.multiselect("Select Products", products, default=products)

# Filter data
filtered_df = df[
    (df['order_date'] >= pd.to_datetime(start_date)) &
    (df['order_date'] <= pd.to_datetime(end_date)) &
    (df['product'].isin(selected_products))
]

# Main app
st.title("Sales Data Dashboard")

# Display filtered data
st.write("### Filtered Data")
st.write(filtered_df)

# Total revenue
total_revenue = filtered_df['quantity'].mul(filtered_df['price']).sum()
st.write("### Total Revenue")
st.write(f"${total_revenue:,.2f}")

# Revenue by product
st.write("### Revenue by Product")
product_revenue = filtered_df.groupby('product').apply(lambda x: (x['quantity'] * x['price']).sum())
st.bar_chart(product_revenue)

# Monthly sales trends
st.write("### Monthly Sales Trends")
filtered_df['month'] = filtered_df['order_date'].dt.to_period('M').astype(str)
monthly_revenue = filtered_df.groupby('month').apply(lambda x: (x['quantity'] * x['price']).sum())
st.line_chart(monthly_revenue)

# Top 5 customers by spending
st.write("### Top 5 Customers by Spending")
top_customers = filtered_df.groupby('customer_id').apply(lambda x: (x['quantity'] * x['price']).sum()).nlargest(5)
st.bar_chart(top_customers)

# Customer segmentation
st.write("### Customer Segmentation")
customer_spending = filtered_df.groupby('customer_id').apply(lambda x: (x['quantity'] * x['price']).sum()).reset_index()
customer_spending.columns = ['customer_id', 'total_spent']

# Perform clustering
kmeans = KMeans(n_clusters=3)
customer_spending['cluster'] = kmeans.fit_predict(customer_spending[['total_spent']])

# Visualize clusters
st.scatter_chart(customer_spending, x='customer_id', y='total_spent', color='cluster')

# Export filtered data
st.write("### Export Data")
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_sales_data.csv',
    mime='text/csv',
)