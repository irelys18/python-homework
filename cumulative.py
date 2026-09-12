import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connect to the SQLite database
connection = sqlite3.connect("db/lesson.db")


# SQL query to calculate the total price for each order
query = """
SELECT o.order_id,
       SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l
    ON o.order_id = l.order_id
JOIN products p
    ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""


# Load the SQL results into a Pandas DataFrame
df = pd.read_sql_query(query, connection)


# Close the database connection
connection.close()


# Calculate cumulative revenue
df["cumulative"] = df["total_price"].cumsum()


# Display the DataFrame
print(df)


# Create a line plot
df.plot(
    kind="line",
    x="order_id",
    y="cumulative",
    title="Cumulative Revenue Over Time",
    xlabel="Order ID",
    ylabel="Cumulative Revenue",
    legend=False
)


# Adjust the layout and display the plot
plt.tight_layout()
plt.show()