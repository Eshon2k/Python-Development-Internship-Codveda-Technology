import requests
from bs4 import BeautifulSoup
import csv

# 1. Use a real practice URL
url = 'https://books.toscrape.com/'

print(f"Connecting to {url}...")
response = requests.get(url)

# 2. Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find the correct HTML containers for books
products = soup.find_all('article', class_='product_pod')

print(f"Found {len(products)} products. Writing to CSV...")

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price'])

    for product in products:
        # 4. Target the specific tags for Title and Price
        title = product.find('h3').find('a')['title']
        price = product.find('p', class_='price_color').text
        
        writer.writerow([title, price])
        print(f" - Scraped: {title}")

print("Success! Data saved to products.csv")

