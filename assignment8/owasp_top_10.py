from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://owasp.org/Top10/2025/")

results = []

# Find all links
links = driver.find_elements(By.CSS_SELECTOR, "a")

for link in links:
    text = link.text.strip()

    # Keep only A01 through A10
    if text.startswith("A01:2025") or \
       text.startswith("A02:2025") or \
       text.startswith("A03:2025") or \
       text.startswith("A04:2025") or \
       text.startswith("A05:2025") or \
       text.startswith("A06:2025") or \
       text.startswith("A07:2025") or \
       text.startswith("A08:2025") or \
       text.startswith("A09:2025") or \
       text.startswith("A10:2025"):

        results.append({
            "Title": text,
            "href": link.get_attribute("href")
        })

print(results)

df = pd.DataFrame(results)

print(df)

df.to_csv("owasp_top_10.csv", index=False)

driver.quit()