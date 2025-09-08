from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
import os

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(log_path='NUL')  # Suppress ChromeDriver logs
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.pinterest.com/')
print("[INFO] Please log in manually. You have 60 seconds...")

time.sleep(60)  # Time to manually log in

print("[INFO] Proceeding to load images...")

image_urls = set()
scroll_pause_time = 3
max_scrolls = 50
scroll_count = 0

while len(image_urls) < 100 and scroll_count < max_scrolls:
    driver.execute_script('window.scrollBy(0, 5000);')
    time.sleep(scroll_pause_time)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img')

    for img in img_tags:
        src = img.get('src')
        if src and 'pinimg' in src:
            image_urls.add(src)

    scroll_count += 1
    print(f"[INFO] Scrolled {scroll_count} times – Found {len(image_urls)} images so far...")

image_urls = list(image_urls)[:100]
print(f"[INFO] Collected {len(image_urls)} image URLs.")

# Download images
os.makedirs('pinterest_images', exist_ok=True)

for i, url in enumerate(image_urls):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(f'pinterest_images/image_{i + 1}.jpg', 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image {i + 1}")
    except Exception as e:
        print(f"Failed to download image {i + 1}: {e}")

print("[INFO] Download complete!")
driver.quit()
