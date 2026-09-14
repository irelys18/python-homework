from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


url = "https://owasp.org/www-project-top-ten/"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(url)

# Find the Top 10 links
elements = driver.find_elements(By.XPATH, "//a")

for element in elements:
    text = element.text.strip()
    href = element.get_attribute("href")

    if text:
        print(text, "->", href)

driver.quit()

# Create DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv("owasp_top_10.csv", index=False)

driver.quit()