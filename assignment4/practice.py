import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
#print(s)

data2 = pd.Series(['Tom', 'Li', 'Antonio', 'Mary'], index=[5, 2, 2, 3])
#print(data2)
#print(data2[2])
#print(data2[1]) error

data3 = data2.reset_index()
#print(data3)

import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
##print(df)

data = pd.DataFrame({
    'Name': ['Amara', 'Yulia', 'Carlos'],
    'Age': [24, 27, 22],
    'City': ['New York', 'San Francisco', 'Chicago']
})

more_data = pd.DataFrame({
  'Name': ['Fred', 'Barney'],
  'Age': [57, 55],
  'City': ['Bedrock', 'Bedrock']
})

df = pd.concat([data, more_data], ignore_index=True)
#print(df)

data = {
    "Name": ["Amara", "Yulia", "Carlos"],
    "Height": ["5.5", "unknown", "5.9"],  # "unknown" is not numeric
    "Weight": ["60", "70", "NaN"]        # "NaN" is a missing placeholder
}
df = pd.DataFrame(data)

#print("Before conversion:")
#print(df)

# Replace placeholders with NaN and convert to numeric
df["Height"] = df["Height"].replace("unknown", pd.NA)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

#print("\nAfter conversion to numeric:")
#print(df)

data = {
    "Person": ["Amara", "Yulia", "Carlos", "Dana", "Eve"],
    "Score": [10, np.nan, 20, None, 25],
    "City": ["New York", "Chicago", None, "Boston", "NaN"]
}
df = pd.DataFrame(data)

#print("Original DataFrame:")
#print(df)

# Strategy 1: Fill numeric missing values with a fixed number
df["Score_filled_fixed"] = df["Score"].fillna(0)

# Strategy 2: Fill numeric missing values with the column mean
mean_score = df["Score"].mean()  # ignoring NaNs
df["Score_filled_mean"] = df["Score"].fillna(mean_score)

# Strategy 3: Fill textual missing values with "Unknown"
df["City_filled"] = df["City"].replace("NaN", pd.NA).fillna("Unknown")

#print("\nDataFrame after fillna strategies:")
#print(df)


data = {
    "Name": ["Amara", "Yulia", "Carlos"],
    "Height": ["5.5", "unknown", "5.9"],  # "unknown" is not numeric
    "Weight": ["60", "70", "NaN"]        # "NaN" is a missing placeholder
}
df = pd.DataFrame(data)

# print("Before conversion:")
# print(df)

# # Replace placeholders with NaN and convert to numeric
# df["Height"] = df["Height"].replace("unknown", pd.NA)
# df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
# df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

# print("\nAfter conversion to numeric:")
# print(df)

data = {
    "Person": ["Amara", "Yulia", "Carlos", "Dana", "Eve"],
    "Score": [10, np.nan, 20, None, 25],
    "City": ["New York", "Chicago", None, "Boston", "NaN"]
}
df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)

# Strategy 1: Fill numeric missing values with a fixed number
# df["Score_filled_fixed"] = df["Score"].fillna(0)
# print(df)

# Strategy 2: Fill numeric missing values with the column mean
# mean_score = df["Score"].mean()  # ignoring NaNs
# df["Score_filled_mean"] = df["Score"].fillna(mean_score)
# print(df)

# Strategy 3: Fill textual missing values with "Unknown"
# df["City_filled"] = df["City"].replace("NaN", pd.NA).fillna("Unknown")
# print(df)

# print("\nDataFrame after fillna strategies:")
# print(df)

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [100, np.nan, 150, np.nan, 200]
}
df = pd.DataFrame(data)

# print("Original Sales Data:")
# print(df)

# Forward fill (propagate last valid observation forward)
# df_ffill = df.copy()
# df_ffill["Sales"] = df_ffill["Sales"].fillna(method="ffill")

# # Backward fill (use next valid observation to fill gaps)
# df_bfill = df.copy()
# df_bfill["Sales"] = df_bfill["Sales"].fillna(method="bfill")

# print("\nForward Fill Result:")
# print(df_ffill)

# print("\nBackward Fill Result:")
# print(df_bfill)

# data = {
#     "Department": [" SALES ", "   HR", "FinanCe  ", "Sales", "MARKETING "],
#     "Location": [" New York ", " Boston", "Chicago   ", "  Boston ", "LOS ANGELES"]
# }
# df = pd.DataFrame(data)

# print("Original DataFrame:")
# print(df)

# # Strip whitespace
# df["Department"] = df["Department"].str.strip()
# df["Location"] = df["Location"].str.strip()

# # Convert columns to uppercase
# df["Department_upper"] = df["Department"].str.upper()
# df["Location_upper"] = df["Location"].str.upper()

# # Or lowercase, if you prefer
# df["Department_lower"] = df["Department"].str.lower()

# print("\nAfter text standardization:")
# print(df)

# Sample data with dates in various formats and some invalid values
# data = {
#     "Event": ["Project Start", "Client Meeting", "Beta Release", "Final Launch", "End of Support"],
#     "Date": ["2021/01/15", "2021-02-27", "03-15-2021", "April 30, 2021", "April 31, 2022"]  # Some invalid or unusual dates
# }
# df = pd.DataFrame(data)

# print("Before conversion:")
# print(df)

# # Convert 'Date' to datetime
# # errors="coerce" will turn invalid dates into NaT (Not a Time)
# df["Date_converted"] = pd.to_datetime(df["Date"], errors="coerce")

# print("\nAfter converting to datetime:")
# print(df)

# # You can check how many values became NaT (invalid dates)
# num_invalid_dates = df["Date_converted"].isna().sum()
# print(f"\nNumber of invalid dates converted to NaT: {num_invalid_dates}")

# # You can use format='mixed' if you have dates in multiple formats
# df["More_dates_converted"] = pd.to_datetime(df["Date"], format='mixed', errors="coerce")

# print("\nAfter converting to datetime:")
# print(df)

# # Check how many were converted again
# num_invalid_dates = df["More_dates_converted"].isna().sum()
# print(f"\nNumber of invalid dates converted to NaT: {num_invalid_dates}")

# Create a sample DataFrame
# data = {
#     'Name': ['Amara', 'Yulia', 'Carlos'],
#     'Age': [26, 31, 36],
#     'City': ['New York', 'Los Angeles', 'Chicago'],
#     'Salary': [70000, 80000, 90000]
# }
# df = pd.DataFrame(data)

# # Save the DataFrame to a CSV file
# df.to_csv("employees.csv", index=False)

# print("DataFrame saved to employees.csv")

df = pd.read_csv('data.csv')
print(df.head())