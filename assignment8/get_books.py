# Task 3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
from selenium.webdriver.common.by import By

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(url)

# Step 3: Find all search result li elements
books = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

print("Number of search results:", len(books))

# Step 4: Create empty results list
results = []

# Step 5: Extract information from each book
books = driver.find_elements(
    By.CSS_SELECTOR, "li.cp-search-result-item"
)

for book in books:

    title = book.find_element(
        By.CSS_SELECTOR, ".title-content"
    ).text

    authors = book.find_elements(
        By.CSS_SELECTOR, ".author-link"
    )

    author = ";".join(a.text for a in authors)

    format_year = book.find_element(
        By.CSS_SELECTOR, ".display-info-primary"
    ).text

    results.append({
        "Title": title,
        "Author": author,
        "Format-Year": format_year
    })

print(results)

#Step 6: Create DataFrame from results list
df = pd.DataFrame(results)

print(df)

# Task 4.1: Write DataFrame to CSV
df.to_csv("get_books.csv", index=False)

# Task 4.2: Write results list to JSON
with open("get_books.json", "w") as json_file:
    json.dump(results, json_file, indent=4)