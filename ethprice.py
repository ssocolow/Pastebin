#print the current eth price using coinmarketcap.com

from bs4 import BeautifulSoup
import requests
page = requests.get("https://coinmarketcap.com/currencies/ethereum/")

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find('div', class_='priceValue___11gHJ').get_text()

print(price)
