import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/p/pl?N=100007709%20601359415'

def update():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_gpus = soup.find_all('div', class_='item-cell')

    file = open('gpu_data.csv', 'w')
    writer = csv.writer(file)

    # Create title row
    writer.writerow(['Product Name', 'Price', 'Availability'])

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_gpus = soup.find_all('div', class_='item-cell') 

    for item in all_gpus:
        title_elem = item.find('a', class_='item-title').text.strip()
        price_elem = item.find('li', class_='price-current').find('strong').text + item.find('li', class_='price-current').find('sup').text.strip()
        stock_elem = item.find('p', class_='item-promo')
        stock_bool = True

        if stock_elem != None:
            stock_elem = stock_elem.text.strip()
            if stock_elem == 'OUT OF STOCK':
                stock_bool = False

        writer.writerow([title_elem, price_elem, stock_bool])
    file.close()