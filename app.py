import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize WebDriver (ensure the ChromeDriver path is set correctly)
chrome_driver_path = "/Users/antonyjalappat/Internship/scraping/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# URL of the Amazon page to scrape
url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
driver.get(url)

# Data lists for storing product details
product_names = []
prices = []
ratings = []
sellers = []
time.sleep(3)
# Define a function to extract product details with added scrolling and waiting
def get_product_details():
    # Scroll down to load more products

    
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    
    for product in products:

        try:
            
            # Product Name
            name = product.find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']").text
        except NoSuchElementException:
            name = None

        try:
            # Price
            price = product.find_element(By.XPATH, ".//span[@class='a-price']").text

        except NoSuchElementException:
            price = None
        if price == None:
            continue 

        try:
            # Rating
            rating = product.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']").text
        except NoSuchElementException:
            rating = None

        try:
            # Open product page and extract seller name
            product_link = product.find_element(By.XPATH, ".//a[@class='a-link-normal s-no-outline']").get_attribute("href")
            driver.execute_script("window.open(arguments[0]);", product_link)
            driver.switch_to.window(driver.window_handles[1])
            
            # Extract Seller Name from product page
            try:
                seller = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="tabular-buybox"]/div[1]/div[6]/div/span'))
                ).text
            except (NoSuchElementException, TimeoutException):
                seller = None

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except NoSuchElementException:
            seller = None

        # Append details to respective lists if name exists
        if name:
            product_names.append(name)
            prices.append(price)
            ratings.append(rating)
            sellers.append(seller)

# Scrape data from multiple pages
num_pages = 2  # Number of pages to scrape
for page in range(num_pages):
    print(f"Scraping page {page + 1}...")
    get_product_details()
    
    # Try to click the "Next" button if it exists, else break the loop
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[35]/div/div/span/a[3]'))
        )
        next_button.click()
        time.sleep(3)  # Wait for the page to load
    except (NoSuchElementException, TimeoutException):
        print("No more pages found.")
        break

# Close the WebDriver
driver.quit()

# Save data to CSV
df = pd.DataFrame({
    "Product Name": product_names,
    "Price": prices,
    "Rating": ratings,
    "Seller Name": sellers
})
df.to_csv("amazon_products.csv", index=False)

print("Data has been saved to amazon_products.csv")
