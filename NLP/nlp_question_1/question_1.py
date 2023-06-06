import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options to run the WebDriver in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Initialize Chrome WebDriver with the configured options
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=9TpObbM6-zE"

# Open the video page
driver.get(video_url)

# Scroll to the end of the page to load all comments
scroll_pause_time = 2
last_height = driver.execute_script(
    "return document.documentElement.scrollHeight")
while True:
    driver.execute_script(
        "window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script(
        "return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find the comment elements
comment_elements = driver.find_elements(By.CSS_SELECTOR, "#content-text")

# Extract the comments
comments = [comment.text for comment in comment_elements]

# Close the WebDriver
driver.quit()

# Create a pandas dataframe with the comments
df = pd.DataFrame(comments, columns=["Comment"])

# Save the dataframe to a CSV file
output_file = "comments.csv"
df.to_csv(output_file, index=False)

print("Comments extracted and saved to", output_file)
