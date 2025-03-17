import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/sales_data.csv')

# Calculate revenue by product
product_revenue = df.groupby('product').apply(lambda x: (x['quantity'] * x['price']).sum())

# Plot
plt.figure(figsize=(10, 6))
product_revenue.plot(kind='bar', color='skyblue')
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('visuals/revenue_by_product.png')
plt.show()


#lineChart

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Extract month and year
df['month'] = df['order_date'].dt.to_period('M').astype(str)

# Calculate monthly revenue
monthly_revenue = df.groupby('month').apply(lambda x: (x['quantity'] * x['price']).sum())

# Plot
plt.figure(figsize=(10, 6))
monthly_revenue.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('visuals/monthly_sales_trends.png')
plt.show()

## Calculate total spending by customer
customer_spending = df.groupby('customer_id').apply(lambda x: (x['quantity'] * x['price']).sum()).nlargest(5)

# Plot
plt.figure(figsize=(10, 6))
customer_spending.plot(kind='bar', color='orange')
plt.title('Top 5 Customers by Spending')
plt.xlabel('Customer ID')
plt.ylabel('Total Spending')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('visuals/top_customers.png')
plt.show()

## Calculate total spending by customer
customer_spending = df.groupby('customer_id').apply(lambda x: (x['quantity'] * x['price']).sum()).nlargest(5)

# Plot
plt.figure(figsize=(10, 6))
customer_spending.plot(kind='bar', color='orange')
plt.title('Top 5 Customers by Spending')
plt.xlabel('Customer ID')
plt.ylabel('Total Spending')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('visuals/top_customers.png')
plt.show()

# Calculate total quantity sold by product
product_quantity = df.groupby('product')['quantity'].sum()

# Plot
plt.figure(figsize=(10, 6))
product_quantity.plot(kind='bar', color='purple')
plt.title('Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('visuals/quantity_by_product.png')
plt.show()

#Clusters

from sklearn.cluster import KMeans

# Calculate total spending by customer
customer_spending = df.groupby('customer_id').apply(lambda x: (x['quantity'] * x['price']).sum()).reset_index()
customer_spending.columns = ['customer_id', 'total_spent']

# Perform clustering
kmeans = KMeans(n_clusters=3)
customer_spending['cluster'] = kmeans.fit_predict(customer_spending[['total_spent']])

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(customer_spending['customer_id'], customer_spending['total_spent'], c=customer_spending['cluster'], cmap='viridis')
plt.title('Customer Segmentation')
plt.xlabel('Customer ID')
plt.ylabel('Total Spending')
plt.colorbar(label='Cluster')
plt.tight_layout()

# Save the plot
plt.savefig('visuals/customer_segmentation.png')
plt.show()

#pieChart

# Calculate total revenue by product
product_revenue = df.groupby('product').apply(lambda x: (x['quantity'] * x['price']).sum())

# Plot
plt.figure(figsize=(8, 8))
product_revenue.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Product')
plt.ylabel('')  # Hide the y-label
plt.tight_layout()

# Save the plot
plt.savefig('visuals/sales_distribution.png')
plt.show()

