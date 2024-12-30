import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Set up Selenium to load the page and scroll
def scrape_image_urls(url, total_images=300):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    image_urls = set()
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while len(image_urls) < total_images:
        # Scroll down to load more images
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Give time for the page to load
        
        # Find image elements and extract URLs
        images = driver.find_elements(By.CSS_SELECTOR, 'img.photo-item__img')
        for img in images:
            img_url = img.get_attribute('src')
            if img_url and img_url.startswith('https://'):
                image_urls.add(img_url)

        # Check if the page height has changed, stop if no more content is loaded
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    driver.quit()

    return list(image_urls)[:total_images]

# Step 2: Download the images from URLs
def download_images(image_urls, save_directory):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    for idx, img_url in enumerate(image_urls):
        try:
            print(f"Downloading image {idx + 1}/{len(image_urls)}: {img_url}")
            response = requests.get(img_url)
            
            if response.status_code == 200:
                image_path = os.path.join(save_directory, f'image_{idx + 1}.jpg')
                with open(image_path, 'wb') as file:
                    file.write(response.content)
            else:
                print(f"Failed to download image {idx + 1}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {idx + 1}: {e}")

# Example usage
url = 'https://www.pexels.com/search/cat/'
save_directory = 'pixel_cat_images'
total_images = 300

# Scrape the URLs
image_urls = scrape_image_urls(url, total_images)

# Download the images if URLs were found
if image_urls:
    print(f"Found {len(image_urls)} images.")
    download_images(image_urls, save_directory)
else:
    print("No images found.")
