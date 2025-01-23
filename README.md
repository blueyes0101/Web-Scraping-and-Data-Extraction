# Web Scraping and Data Extraction Using Selenium

## Project Objective
The goal of this project is to create a bot using Selenium that interacts with a website's search box, retrieves results, and extracts detailed information. The project is designed to be adaptable to any website and follows a general structure.

---

## Project Requirements

### Software Requirements
- Python 3.10 or later
- Google Chrome or Chromium
- Chromedriver (compatible with the installed Google Chrome/Chromium version)

### Python Packages
Install the required libraries using the following command:
```bash
pip install selenium undetected-chromedriver
```

---

## Setup

### 1. Install Chromedriver and Browser
- **Chromedriver**: Download the appropriate version and add it to the `PATH`.
- **Google Chrome/Chromium**: Ensure the browser is installed on your system.

To verify the browser and Chromedriver installation, run the following command:
```bash
which google-chrome  # or chromium
```

### 2. Project Folder Structure
The project directory should follow this structure:
```
my_selenium_bot/
|-- bot.py  # Main Python script
|-- requirements.txt  # Required Python packages
|-- README.md  # Technical documentation
```

---

## How the Bot Works

### 1. Access the Website
The bot securely accesses the target website using Selenium and `undetected-chromedriver`.

### 2. Input Data into the Search Box
The bot locates the search box using a CSS selector or XPath and inputs the search query.

### 3. Handle Dropdown Suggestions
If the search box provides a dropdown, the bot selects the first suggestion.

### 4. Retrieve and Save Results
The bot extracts search results and saves detailed information to a file.

---

## Main Python Code
Below is a template for the bot:

```python
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
```

---

## Challenges Encountered and Solutions

### Challenge 1: Element Not Interactable
**Problem:** The bot attempted to interact with an element that was either not visible or not ready.

**Solution:** Use `WebDriverWait` and `expected_conditions` to ensure the element is clickable before interacting with it.
```python
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']"))
)
```

### Challenge 2: Dropdown Menu Not Appearing
**Problem:** The dropdown menu did not appear despite input being entered.

**Solution:** Wait for the dropdown menu to load and ensure it is visible before selecting an option.
```python
dropdown_results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.typeahead.dropdown-menu li a"))
)
if dropdown_results:
    dropdown_results[0].click()
```

### Challenge 3: Deprecation of `find_element_by_*`
**Problem:** Older methods like `find_element_by_css_selector` were no longer supported in the latest Selenium versions.

**Solution:** Switch to the updated `find_element` method with `By` selectors:
```python
search_box = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
```

### Challenge 4: Browser Path Issues
**Problem:** The browser binary location was not automatically detected.

**Solution:** Specify the exact path to the browser binary in the Chrome options:
```python
options.binary_location = "/opt/google/chrome/google-chrome"
```


---

## Project Files
- **`bot.py`**: Main Python script for the bot.
- **`requirements.txt`**:
  ```
  selenium
  undetected-chromedriver
  ```
- **`README.md`**: Documentation (this file).

---

## Future Enhancements
1. **Save Data in CSV Format:** Store the results in a `.csv` file for better organization.
2. **Pagination Handling:** Add functionality to navigate through multiple pages of search results.
3. **Error Handling:** Implement advanced error handling and logging mechanisms.

