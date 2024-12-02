from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random

def fetch_page_content(url):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration.
    chrome_options.add_argument("--no-sandbox")  # Required for Chrome to work in headless mode on some OS.
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents detection as an automated bot.
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Set a user-agent to mimic a real browser
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    )

    # Initialize Selenium with options
    driver = webdriver.Chrome(options=chrome_options)

    # Open the target URL
    driver.get(url)

    # Random delays to mimic human interaction
    time.sleep(random.uniform(3, 5))

    # Scroll down the page to mimic human reading behavior
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1, 3))
    driver.execute_script("window.scrollTo(0, 0);")

    # Give the page some time to load fully
    time.sleep(random.uniform(3, 5))

    try:
        # Extract the page content
        data = driver.find_element(By.TAG_NAME, "body").text
    except Exception as e:
        print("Error extracting content:", e)
        data = None
    finally:
        # Close the browser
        driver.quit()

    return data

# Example usage:
# url = "https://www.upwork.com/freelance-jobs/apply/AWS-Lambda-API-Bug-Fix-Needed-Node_~021849158770878375599/"
# content = fetch_page_content(url)
# print(content)
