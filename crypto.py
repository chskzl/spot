#!/bin/python

# Displays bitcoin, ethereum, dogecoin, and 0x spot prices on a single line

from bs4 import BeautifulSoup
import requests

cryptos = []

spot = requests.get('https://www.coindesk.com')

soup = BeautifulSoup(spot.text, 'lxml')

for coin in soup.find_all('div', class_='pricing-col'):
	name = coin.a.div.div.div.span.strong.text
	if name == "Bitcoin" or name == "Ethereum" or name == "Dogecoin" or name == "0x":
		if name == "Bitcoin":
			name = "BTC"
		if name == "Ethereum":
			name = "ETH"
		if name == "Dogecoin":
			name = "DOGE"
		price = coin.find('div', class_="price").text
		change = coin.find('div', class_="change-value").text
		cryptos.append(name + " " + price + " (" + change[:-1] + ")")

for line in cryptos[:-1]:
	print(line, end=" | ")
print(cryptos[-1])
