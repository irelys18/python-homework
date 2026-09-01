import sqlite3
import pandas as pd


connection = sqlite3.connect("../db/lesson.db")

query = """
SELECT
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products
    ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, connection)

print(df.head())

df["total"] = df["quantity"] * df["price"]

summary = df.groupby("product_id").agg(
    line_item_count=("line_item_id", "count"),
    total=("total", "sum"),
    product_name=("product_name", "first")
).reset_index()

summary = summary.sort_values("product_name")

print(summary)

summary.to_csv("order_summary.csv", index=False)