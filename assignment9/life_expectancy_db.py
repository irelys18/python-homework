import sqlite3
import pandas as pd

# Load the cleaned/transformed Life Expectancy CSV
df = pd.read_csv("../csv/Life Expectancy Data.csv")

print("BEFORE CLEANING")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Clean the data
df = df.drop_duplicates()

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from Country names
df["Country"] = df["Country"].str.strip()

# Fill missing numeric values with the median
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Feature engineering
df["GDP Category"] = pd.qcut(
    df["GDP"],
    q=4,
    labels=["Low", "Medium", "High", "Very High"]
)

df["Vaccination Rate"] = (
    df["Hepatitis B"]
    + df["Polio"]
    + df["Diphtheria"]
) / 3

df["Adult Survival"] = 1000 - df["Adult Mortality"]

df["Life_Expectancy_Category"] = pd.cut(
    df["Life expectancy"],
    bins=[0, 60, 70, 80, 100],
    labels=["Low", "Moderate", "High", "Very High"]
)

df["GDP_per_Person"] = df["GDP"] / df["Population"]

print("\nAFTER CLEANING AND TRANSFORMATION")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())

# Connect to SQLite database
connection = sqlite3.connect("life_expectancy.db")

# Save the cleaned/transformed DataFrame to SQLite
df.to_sql(
    "life_expectancy",
    connection,
    if_exists="replace",
    index=False
)

# Verify the database
print("\nDATA IN SQLITE DATABASE")
result = pd.read_sql_query(
    "SELECT * FROM life_expectancy LIMIT 5;",
    connection
)

print(result)

# Verify number of rows
count = pd.read_sql_query(
    "SELECT COUNT(*) AS total_rows FROM life_expectancy;",
    connection
)

print("\nTOTAL ROWS IN SQLITE DATABASE")
print(count)

connection.close()

print("\nLife Expectancy database created successfully!")