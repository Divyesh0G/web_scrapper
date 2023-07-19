import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

csv_Zip_path = os.path.join(os.path.dirname(__file__),'csv','uszips.csv')

try:
    os.path.isfile(csv_Zip_path)
    print()
    print('Reading the Zip codes....')
    print()
except:
    print('No csv file with Zip code')
    exit

reader = pd.read_csv(csv_Zip_path,encoding='utf-8',header=0)
Zip_code = reader['zip']

tst_zip = 98002


url = f'https://search.earth911.com/?what=%234+Rigid+Plastics&where={tst_zip}&max_distance=25'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


resp = requests.get(url,headers)

bs = BeautifulSoup(resp.content,'lxml')

num_of_pages = bs.find()

card = bs.find('ul', class_='result-list').findAll('li')

for i in card:
    name = (i.find('div',class_='description').text).strip()
    typ = i.find('span',class_='type').text
    area1 = i.find('p',class_='address1').text
    area2 = i.find('p',class_='address2').text
    area3 = i.find('p',class_='address3').text
    phone = i.find('p',class_='phone').text
    print(f'name:{name},\nType:{typ},\nAddress1:{area1},\nAddress2:{area2},\nAddress3:{area3},\nPhone:{phone}\n\n')
  