import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5433",
    dbname="data_visualization", 
    user="postgres",
    password="5432"
)

queries = {
    "1. Orders by status": """
        SELECT order_status, COUNT(*) AS order_count
        FROM olist_orders_dataset
        GROUP BY order_status
        ORDER BY order_count DESC;
    """,

    "2. Average price and freight": """
        SELECT ROUND(AVG(price), 2) AS avg_price, ROUND(AVG(freight_value), 2) AS avg_freight
        FROM olist_order_items_dataset;
    """,

    "3. Payments by type": """
        SELECT payment_type, COUNT(*) AS count
        FROM olist_order_payments_dataset
        GROUP BY payment_type
        ORDER BY count DESC;
    """,

    "4. Average review score": """
        SELECT ROUND(AVG(review_score), 2) AS average_review_score
        FROM olist_order_reviews_dataset;
    """,

    "5. Top 10 cities by customers": """
        SELECT customer_city, COUNT(*) AS customer_count
        FROM olist_customers_dataset
        GROUP BY customer_city
        ORDER BY customer_count DESC
        LIMIT 10;
    """,

    "6. Order status and item count (first 10)": """
        SELECT o.order_id, o.order_status, COUNT(*) AS items_count
        FROM olist_orders_dataset o
        INNER JOIN olist_order_items_dataset i ON o.order_id = i.order_id
        GROUP BY o.order_id, o.order_status
        LIMIT 10;
    """,

    "7. Orders and review score (first 10)": """
        SELECT o.order_id, r.review_score
        FROM olist_orders_dataset o
        LEFT JOIN olist_order_reviews_dataset r ON o.order_id = r.order_id
        LIMIT 10;
    """,

    "8. Orders with 'beleza_saude' products": """
        SELECT COUNT(DISTINCT o.order_id) AS beauty_orders
        FROM olist_order_items_dataset i
        JOIN olist_products_dataset p ON i.product_id = p.product_id
        JOIN olist_orders_dataset o ON o.order_id = i.order_id
        WHERE p.product_category_name = 'beleza_saude';
    """,

    "9. Sellers with orders (first 10)": """
        SELECT 
            s.seller_id,
            s.seller_city,
            i.order_id,
            i.price
        FROM olist_sellers_dataset s
        RIGHT JOIN olist_order_items_dataset i ON s.seller_id = i.seller_id
        LIMIT 10;
    """,

    "10. Orders with items (first 10)": """
        SELECT 
            o.order_id,
            o.order_status,
            i.product_id,
            i.price
        FROM olist_orders_dataset o
        JOIN olist_order_items_dataset i ON o.order_id = i.order_id
        LIMIT 10;
    """
}

with conn.cursor() as cur:
    for title, query in queries.items():
        print(f"\n=== {title} ===")
        df = pd.read_sql_query(query, conn)
        print(df)

conn.close()
