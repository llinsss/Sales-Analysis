-- Query 1: Total Revenue
SELECT SUM(quantity * price) AS total_revenue FROM sales;

-- Query 2: Top 5 Customers by Spending
SELECT customer_id, SUM(quantity * price) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;

-- Query 3: Monthly Sales Trends
SELECT strftime('%Y-%m', order_date) AS month, SUM(quantity * price) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Query 4: Most Popular Product
SELECT product, SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY product
ORDER BY total_quantity_sold DESC
LIMIT 1;