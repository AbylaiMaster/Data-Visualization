# AbyMarket: E-commerce Data Analytics

**AbyMarket** - a Kazakhstan-based branch of a large e-commerce marketplace connecting sellers and buyers across the country.

This project is focused on performing data analytics for AbyMarket using sales, payments, customer, and review data. The goal is to identify trends in customer behavior, product categories, order statuses, and satisfaction, in order to support data-driven decision-making and improve business performance.

---

## Analysis Overview

- 6 meaningful data visualizations using SQL with multiple JOINs (matplotlib)
- Interactive time slider chart using Plotly
- Excel export with filters, conditional formatting, frozen headers, and color gradient
- All data is queried from a PostgreSQL database using `psycopg2`

---

## ER Diagram

![image](https://github.com/AbylaiMaster/Data-Visualization/blob/main/ERD.png)

---

## How to Run the Project

### 1. Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- Required Python libraries

---

### 2. Install Required Libraries

```bash
pip install pandas psycopg2 matplotlib plotly openpyxl
```

---

### 3. Prepare the PostgreSQL Database

Make sure your PostgreSQL database contains the following tables (from the Olist dataset):

- `olist_orders_dataset`
- `olist_order_items_dataset`
- `olist_order_payments_dataset`
- `olist_order_reviews_dataset`
- `olist_customers_dataset`
- `olist_products_dataset`
- `olist_sellers_dataset`

You can import them from CSV files using PostgreSQL's `COPY` command or a tool like DBeaver.

---

### 4. Configure the Connection

Open `analytics.py` and update the PostgreSQL connection parameters:

```python
conn = psycopg2.connect(
    host="localhost",
    port="5433",
    dbname="your_database_name",
    user="your_username",
    password="your_password"
)
```

---

### 5. Run the Analytics Script

```bash
python analytics.py
```

The script will:

- Run multiple SQL queries with JOINs
- Create and save 6 static graphs to `/charts/`
- Show an interactive Plotly graph with time slider
- Export data into a styled Excel file in `/exports/`

---

### 6. Tools and Resources Used

- Python 3
- PostgreSQL
- pandas — for data manipulation
- matplotlib — for static visualizations
- plotly — for interactive visualizations
- openpyxl — for Excel export and formatting
- psycopg2 — for PostgreSQL connection

---

### Dataset Source

Olist Dataset:  
[Olist Brazilian E-Commerce Public Dataset on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
