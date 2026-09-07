import sqlite3
import pandas as pd

# Load raw CSV data
df = pd.read_csv("../assignment8/get_books.csv")

print("BEFORE CLEANING")
print(df)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Clean the data
df = df.drop_duplicates()

df["Title"] = df["Title"].str.strip()
df["Author"] = df["Author"].str.strip()
df["Format-Year"] = df["Format-Year"].str.strip()

# Split Format-Year into two columns
df[["Format", "Year"]] = df["Format-Year"].str.split(
    ", ", expand=True
)

# Convert Year to numeric
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Remove the original combined column
df = df.drop(columns=["Format-Year"])

print("\nAFTER CLEANING")
print(df)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Connect to SQLite database
connection = sqlite3.connect("capstone.db")

# Save DataFrame to SQLite
df.to_sql("books", connection, if_exists="replace", index=False)

# Verify the database table
print("\nDATA IN SQLITE DATABASE")
print(pd.read_sql_query("SELECT * FROM books", connection))

connection.close()

print("\nDatabase created successfully!")