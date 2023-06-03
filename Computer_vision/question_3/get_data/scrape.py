import os
import time
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape(keyword):
    # Set Chrome options to run the WebDriver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Set path to chromedriver as per your configuration
    webdriver_service = Service(ChromeDriverManager().install())

    # Initialize Chrome WebDriver with the configured options
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # Website URL
    url = 'https://www.flipkart.com/search?q={q}'
    search_query = keyword

    # Create a directory to save the images
    save_directory = 'image_data/'+ keyword
    os.makedirs(save_directory, exist_ok=True)

    # Scrape images from multiple pages
    num_pages = 30
    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}...")
        driver.get(url.format(q=search_query) + f"&page={page}")

        # Scroll to the end of the page to load all images
        scroll_pause_time = 5
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Find the images on the page
        img_results = driver.find_elements(By.XPATH, "//img[@class='_396cs4']")
        print(f'Found {len(img_results)} images on page {page}')

        # Download and save the images
        for i, img in enumerate(img_results):
            img_url = img.get_attribute('src')
            response = requests.get(img_url)
            img_data = response.content
            image = Image.open(BytesIO(img_data))
            image.save(os.path.join(save_directory, f'page_{page}_image_{i}.jpg'))
            print(f'Saved page_{page}_image_{i}.jpg')

    # Close the WebDriver
    driver.quit()

keyword = 'smarttv'

scrape(keyword)