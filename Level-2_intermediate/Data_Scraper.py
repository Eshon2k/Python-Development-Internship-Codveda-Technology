import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://example.com/products'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product containers (adjust the tag and class as per the website structure)
products = soup.find_all('div', class_='product')

# Open a CSV file to write the extracted data
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Price'])
    
    # Loop through each product and extract title and price
    for product in products:
        title = product.find('h2', class_='title').text.strip()
        price = product.find('span', class_='price').text.strip()
        # Write the extracted data to the CSV file
        writer.writerow([title, price])

