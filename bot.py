import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome options
options = uc.ChromeOptions()
options.binary_location = "/opt/google/chrome/google-chrome"  # Specify the browser path

# Launch the browser
driver = uc.Chrome(options=options)

# Navigate to the target website
site_url = "https://example.com"  # Replace with the target website's URL
driver.get(site_url)

# Locate the search box and input the query
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']"))  # CSS selector for the search box
    )
    search_box.send_keys("example query")  # Input the search query
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)  # Press Enter
except Exception as e:
    print(f"Error: {e}")

# Locate and print search results
try:
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "result-item"))  # Class name for result items
    )
    print("Results:")
    for result in results:
        print(result.text)
except Exception as e:
    print(f"Error retrieving results: {e}")

# Close the browser
driver.quit()
