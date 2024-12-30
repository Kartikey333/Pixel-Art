import os
import requests
from bs4 import BeautifulSoup

def scrape_image_urls(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the image elements
    image_tags = soup.find_all('img', class_='photo-item__img')
    
    # Extract the URLs of the images
    image_urls = [img['src'] for img in image_tags if img.has_attr('src')]
    
    return image_urls

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

image_urls = scrape_image_urls(url)

if image_urls:
    print(f"Found {len(image_urls)} images.")
    download_images(image_urls, save_directory)
else:
    print("No images found.")
