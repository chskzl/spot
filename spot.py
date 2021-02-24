#!/bin/python

from bs4 import BeautifulSoup
import requests

spot = requests.get('http://widgets.apmex.com/widget/spotprice/?w=280&amp;h=180&amp;mtls=GSPL&amp;arf=False&amp;rint=5&amp;srf=False&amp;tId=1&amp;cId=fd9762f2-d15f-4141-9931-89fc33dfff60&amp;wId=1')

soup = BeautifulSoup(spot.text, 'lxml')

jndex = 0
for metal in soup.find_all('tr'):
	metal_name = ""
	spot_price = ""
	change = ""
	index = 0

	for col in metal.find_all('td'):
		if index == 0:
			metal_name = col.text.strip()
		if index == 2:
			spot_price = col.text.strip()
		if index == 3:
			change = col.text.strip()
			if change[0] == '(':
				change = change[1:-1]
			if change[0] != '-':
				change = "+" + change
		index += 1

	if metal_name != "" and jndex < 8:
		print(metal_name.ljust(12," ") + spot_price.rjust(10," ") + " (" + change[0] + change[2:] + ")")
	jndex += 1

spot = requests.get('https://www.coindesk.com')

soup = BeautifulSoup(spot.text, 'lxml')

for coin in soup.find_all('div', class_='pricing-col'):
	name = coin.a.div.div.div.span.strong.text
	if name == "Bitcoin" or name == "Ethereum" or name == "Dogecoin" or name == "0x":
		price = coin.find('div', class_="price").text
		change = coin.find('div', class_="change-value").text
		print(name.ljust(12," ") + price.rjust(10," ") + " (" + change[:-1] + ")")
