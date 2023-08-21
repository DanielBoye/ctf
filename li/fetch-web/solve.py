from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# Modify the URL to point to your local server
BASE_URL = "http://localhost:4242"

def upload_malicious_html():
    url = f"{BASE_URL}/runHTML"
    files = {'file': ('malicious.html', '<your malicious HTML content here>', 'text/html')}
    response = requests.post(url, files=files)
    return response.text.strip()

def get_flag_screenshot(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    screenshot_path = "flag_screenshot.png"
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

def extract_flag_from_screenshot(screenshot_path):
    # Your code here to extract the flag from the screenshot
    # You may use Python libraries like Pillow or OpenCV to process the image

def solve_ctf_challenge():
    # Upload malicious HTML file to the server
    uploaded_file_url = upload_malicious_html()

    # Run the HTML file on the server using Puppeteer and get the screenshot
    screenshot_url = f"{BASE_URL}/{uploaded_file_url}"
    flag_screenshot_path = get_flag_screenshot(screenshot_url)

    # Extract the flag from the screenshot
    flag = extract_flag_from_screenshot(flag_screenshot_path)
    print(f"Flag: {flag}")

if __name__ == "__main__":
    solve_ctf_challenge()
