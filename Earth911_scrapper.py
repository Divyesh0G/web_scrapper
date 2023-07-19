import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Define the path to the CSV file containing zip codes
csv_Zip_path = os.path.join(os.path.dirname(__file__), 'csv', 'uszips.csv')

try:
    # Check if the CSV file exists
    os.path.isfile(csv_Zip_path)
    print()
    print('Reading the Zip codes....')
    print()
except:
    print('No CSV file with Zip code')
    exit

# Read the CSV file and retrieve the 'zip' column
reader = pd.read_csv(csv_Zip_path, encoding='utf-8', header=0)
Zip_code = reader['zip']

# Set the test zip code for the location you want to search
tst_zip = 98002

# Construct the URL for the search query
url = f'https://search.earth911.com/?what=%234+Rigid+Plastics&where={tst_zip}&max_distance=25'

# Set the User-Agent header for the HTTP request
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# Send an HTTP GET request to the URL
resp = requests.get(url, headers=headers)

# Parse the response content using BeautifulSoup
bs = BeautifulSoup(resp.content, 'lxml')

# Extract the number of pages from the parsed content
num_of_pages = bs.find()  # Add the appropriate method and parameters

# Find all the search result items
card = bs.find('ul', class_='result-list').findAll('li')

# Iterate over each search result and extract details
for i in card:
    # Extract name
    name = (i.find('div', class_='description').text).strip()
    
    # Extract type
    typ = i.find('span', class_='type').text
    
    # Extract address lines
    area1 = i.find('p', class_='address1').text
    area2 = i.find('p', class_='address2').text
    area3 = i.find('p', class_='address3').text
    
    # Extract phone number
    phone = i.find('p', class_='phone').text
    
    # Print the extracted details
    print(f'name: {name},\nType: {typ},\nAddress1: {area1},\nAddress2: {area2},\nAddress3: {area3},\nPhone: {phone}\n\n')
