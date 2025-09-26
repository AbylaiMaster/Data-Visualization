```bash
AbyMarket - a Kazakhstan-based branch of a large e-commerce marketplace connecting sellers and buyers across the country.

This project is focused on performing data analytics for AbyMarket using sales, payments, customer, and review data. The goal is to identify trends in customer behavior, product categories, order statuses, and satisfaction, in order to support data-driven decision-making and improve business performance.

Analysis:
https://github.com/AbylaiMaster/Data-Visualization/blob/main/ERD.png

How to Run the Project

1. Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- Required Python libraries

2. Install Required Libraries
pip install pandas psycopg2

3. Prepare the PostgreSQL Database
Make sure your PostgreSQL database contains the following tables (from the Olist dataset):
olist_orders_dataset
olist_order_items_dataset
olist_order_payments_dataset
olist_order_reviews_dataset
olist_customers_dataset
olist_products_dataset
olist_sellers_dataset

You can import them from CSV files using PostgreSQL's COPY command or a tool like DBeaver.

4. Configure the Connection
Open analysis.py and update the PostgreSQL connection parameters:
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="your_database_name",
    user="your_username",
    password="your_password"
)
5. Run the Analytics Script
python analysis.py
The script will connect to your PostgreSQL database and print the results of 10 analytical queries to the terminal.

6. Tools and Resources Used
Python 3
PostgreSQL
pandas — for data manipulation
psycopg2 — for connecting to PostgreSQL
Olist Dataset:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce


Olist Dataset:
Olist Brazilian E-Commerce Public Dataset on Kaggle
