import sqlite3

def add_publisher(connection, name):
    try:
        existing = connection.execute(
            "SELECT id FROM publishers WHERE name = ?",
            (name,)
        ).fetchone()

        if existing:
            print(f"Publisher '{name}' already exists.")
            return

        connection.execute(
            "INSERT INTO publishers (name) VALUES (?)",
            (name,)
        )

    except sqlite3.Error as error:
        print("Error adding publisher:", error)


def add_magazine(connection, name, publisher_id):
    try:
        existing = connection.execute(
            "SELECT id FROM magazines WHERE name = ?",
            (name,)
        ).fetchone()

        if existing:
            print(f"Magazine '{name}' already exists.")
            return

        connection.execute(
            """
            INSERT INTO magazines (name, publisher_id)
            VALUES (?, ?)
            """,
            (name, publisher_id)
        )

    except sqlite3.Error as error:
        print("Error adding magazine:", error)


def add_subscriber(connection, name, address):
    try:
        existing = connection.execute(
            """
            SELECT id
            FROM subscribers
            WHERE name = ? AND address = ?
            """,
            (name, address)
        ).fetchone()

        if existing:
            print(f"Subscriber '{name}' already exists.")
            return

        connection.execute(
            """
            INSERT INTO subscribers (name, address)
            VALUES (?, ?)
            """,
            (name, address)
        )

    except sqlite3.Error as error:
        print("Error adding subscriber:", error)


def add_subscription(connection, subscriber_id, magazine_id, expiration_date):
    try:
        existing = connection.execute(
            "SELECT subscription_id FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        ).fetchone()

        if existing:
            print("Subscription already exists.")
            return

        connection.execute(
            """
            INSERT INTO subscriptions
            (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
            """,
            (subscriber_id, magazine_id, expiration_date)
        )

    except sqlite3.Error as error:
        print("Error adding subscription:", error)


try:
    connection = sqlite3.connect("../db/magazines.db")
    connection.execute("PRAGMA foreign_keys = 1")

    # Task 2

    connection.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        )
    """)

    # Task 3 - Add data to the tables

    add_publisher(connection, "Penguin Random House")
    add_publisher(connection, "HarperCollins")
    add_publisher(connection, "Simon & Schuster")

    add_magazine(connection, "National Geographic", 1)
    add_magazine(connection, "Time Magazine", 2)
    add_magazine(connection, "People Magazine", 3)

    add_subscriber(connection, "Maria Garcia", "123 Main Street")
    add_subscriber(connection, "John Smith", "456 Oak Avenue")
    add_subscriber(connection, "Ana Rodriguez", "789 Pine Road")

    add_subscription(connection, 1, 1, "2027-09-01")
    add_subscription(connection, 2, 2, "2027-10-15")
    add_subscription(connection, 3, 3, "2027-12-31")

    connection.commit()

    # View the contents of the database

    print("\nPublishers:")
    rows = connection.execute("SELECT * FROM publishers").fetchall()
    for row in rows:
        print(row)

    print("\nMagazines:")
    rows = connection.execute("SELECT * FROM magazines").fetchall()
    for row in rows:
        print(row)

    print("\nSubscribers:")
    rows = connection.execute("SELECT * FROM subscribers").fetchall()
    for row in rows:
        print(row)

    print("\nSubscriptions:")
    rows = connection.execute("SELECT * FROM subscriptions").fetchall()
    for row in rows:
        print(row)

    # Task 4 - Find magazines for a particular publisher

    print("\nMagazines published by Penguin Random House:")

    query = """
    SELECT magazines.name
    FROM magazines
    JOIN publishers
        ON magazines.publisher_id = publishers.id
    WHERE publishers.name = ?
    """

    rows = connection.execute(query, ("Penguin Random House",))

    for row in rows:
        print(row)

    print("Tables created successfully!")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if "connection" in locals():
        connection.close()
        print("Database connection closed.")