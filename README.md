
# Amazon Product Scraper

This project is a web scraper built with Python and Selenium to extract product details from Amazon. It captures product names, prices, ratings, and seller information from specified pages.

## Features

- Extracts product name, price, rating, and seller information from Amazon search results.
- Supports pagination to scrape multiple pages.
- Saves the extracted data in a CSV file (`amazon_products.csv`).

## Requirements

- Python 3
- [Google Chrome](https://www.google.com/chrome/) browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (ensure it matches your Chrome version)
- Python packages: `selenium`, `pandas`

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/amazon-product-scraper.git
   cd amazon-product-scraper
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up ChromeDriver:
   - [Download ChromeDriver](https://sites.google.com/chromium.org/driver/), matching your installed Chrome version.
   - Place the ChromeDriver executable in your project's directory or specify the path in the code.

4. Update the ChromeDriver path in `app.py`:
   ```python
   chrome_driver_path = "/path/to/your/chromedriver"
   ```

## Usage

1. Run the scraper:
   ```bash
   python app.py
   ```

2. The scraper will open the specified Amazon page and begin extracting product data. After scraping the defined number of pages, it will save the data to `amazon_products.csv`.

## Code Explanation

- **`get_product_details()`**: A function that extracts product details (name, price, rating, and seller) from each product on the page.
- **Pagination**: The scraper navigates through multiple pages by clicking the "Next" button until the specified number of pages (`num_pages`) is reached or there are no more pages.
- **Data Storage**: Data is stored in lists and then converted to a DataFrame using `pandas` before being saved as a CSV file.

## CSV Output

The CSV file `amazon_products.csv` will contain:
- **Product Name**: The name of the product.
- **Price**: The price of the product.
- **Rating**: The product rating.
- **Seller Name**: The name of the seller.

## Notes

- This scraper is for educational purposes only. Scraping Amazon pages for commercial use may violate Amazon's terms of service. Use this tool responsibly and be aware of the legal and ethical considerations of web scraping.
- Amazon may change its page structure over time, which could require updates to the XPath selectors in the code.

