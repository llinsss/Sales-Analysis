# Sales Data Analysis with SQL

This project analyzes a mock sales dataset using SQLite. The dataset contains information about orders, customers, products, and sales.

## Dataset
The dataset (`sales_data.csv`) contains the following columns:
- `order_id`: Unique ID for each order.
- `customer_id`: Unique ID for each customer.
- `order_date`: Date of the order.
- `product`: Name of the product.
- `quantity`: Quantity of the product sold.
- `price`: Price of the product.

## Queries
1. **Total Revenue**:
   ```sql
   SELECT SUM(quantity * price) AS total_revenue FROM sales;