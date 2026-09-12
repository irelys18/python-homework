import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Connect to the SQLite database
connection = sqlite3.connect("db/lesson.db")


# SQL query to calculate revenue for each employee
query = """
SELECT last_name,
       SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o
    ON e.employee_id = o.employee_id
JOIN line_items l
    ON o.order_id = l.order_id
JOIN products p
    ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""


# Load the SQL results into a Pandas DataFrame
employee_results = pd.read_sql_query(query, connection)


# Close the database connection
connection.close()


# Display the DataFrame
print(employee_results)


# Create a bar chart
employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    title="Employee Revenue",
    xlabel="Employee Last Name",
    ylabel="Revenue",
    legend=False
)


# Adjust the layout and display the plot
plt.tight_layout()
plt.show()
