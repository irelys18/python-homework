import sqlite3

# Task 1: Complex JOINs with Aggregation

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

sql = """
SELECT orders.order_id,
SUM(products.price * line_items.quantity) AS total_price
FROM orders
JOIN line_items
ON orders.order_id = line_items.order_id
JOIN products
ON line_items.product_id = products.product_id
GROUP BY orders.order_id
ORDER BY orders.order_id
LIMIT 5;
"""

cursor.execute(sql)

results = cursor.fetchall()

for row in results:
    print(f"Order ID: {row[0]}, Total Price: {row[1]}")


# Task 2: Understanding Subqueries

sql = """
SELECT customers.customer_name,
AVG(order_totals.total_price) AS average_total_price
FROM customers
LEFT JOIN (
    SELECT orders.customer_id AS customer_id_b,
           SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items
    ON orders.order_id = line_items.order_id
    JOIN products
    ON line_items.product_id = products.product_id
    GROUP BY orders.order_id
) AS order_totals
ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id;
"""

cursor.execute(sql)

results = cursor.fetchall()

for row in results:
    print(f"Customer: {row[0]}, Average Total Price: {row[1]}")


# Task 3: Insert Transaction Based on Data

conn.execute("PRAGMA foreign_keys = 1")

try:
    conn.execute("BEGIN")

    # Find customer
    cursor.execute("""
        SELECT customer_id
        FROM customers
        WHERE customer_name = ?
    """, ("Perez and Sons",))

    customer_id = cursor.fetchone()[0]

    # Find employee
    cursor.execute("""
        SELECT employee_id
        FROM employees
        WHERE first_name = ? AND last_name = ?
    """, ("Miranda", "Harris"))

    employee_id = cursor.fetchone()[0]

    # Find five least expensive products
    cursor.execute("""
        SELECT product_id
        FROM products
        ORDER BY price
        LIMIT 5
    """)

    product_ids = cursor.fetchall()

    # Create the order
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id
    """, (customer_id, employee_id))

    order_id = cursor.fetchone()[0]

    # Add 10 of each product
    for product in product_ids:
        product_id = product[0]

        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
        """, (order_id, product_id, 10))

    conn.commit()

    # Display the newly created line items
    cursor.execute("""
        SELECT line_items.line_item_id,
               line_items.quantity,
               products.product_name
        FROM line_items
        JOIN products
        ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?
    """, (order_id,))

    results = cursor.fetchall()

    for row in results:
        print(
            f"Line Item ID: {row[0]}, "
            f"Quantity: {row[1]}, "
            f"Product: {row[2]}"
        )

except sqlite3.Error as error:
    conn.rollback()
    print("Transaction failed:", error)


# Task 4: Aggregation with HAVING

sql = """
SELECT employees.employee_id,
       employees.first_name,
       employees.last_name,
       COUNT(orders.order_id) AS order_count
FROM employees
JOIN orders
ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id,
         employees.first_name,
         employees.last_name
HAVING COUNT(orders.order_id) > 5;
"""

cursor.execute(sql)

results = cursor.fetchall()

for row in results:
    print(
        f"Employee ID: {row[0]}, "
        f"First Name: {row[1]}, "
        f"Last Name: {row[2]}, "
        f"Order Count: {row[3]}"
    )

conn.close()