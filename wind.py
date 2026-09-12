import plotly.express as px
import plotly.data as pldata


# Load the Plotly wind dataset
df = pldata.wind(return_type="pandas")


# Display the first and last 10 rows
print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))


# Convert wind strength ranges to numeric values
df["strength"] = (
    df["strength"]
    .str.replace("+", "", regex=False)
    .str.split("-")
    .str[0]
    .astype(float)
)


# Create an interactive scatter plot
fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Strength vs Frequency",
    labels={
        "frequency": "Frequency",
        "strength": "Wind Strength",
        "direction": "Direction"
    }
)


# Save the interactive plot as an HTML file
fig.write_html("wind.html")


# Display the plot
fig.show()