from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://owasp.org/www-project-top-ten/"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(url)

# Find the Top 10 links
elements = driver.find_elements(
    By.XPATH,
    "//a[contains(@href, '/Top10/')]"
)

results = []

for element in elements[:10]:
    results.append({
        "title": element.text,
        "href": element.get_attribute("href")
    })

print(results)

# Create DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv("owasp_top_10.csv", index=False)

driver.quit()