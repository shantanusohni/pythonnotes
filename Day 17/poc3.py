import requests

baseurl = 'https://www.nseindia.com/get-quotes/equity?symbol='
symbols = ['INFY', 'ZENSARTECH', 'TCS']

for symbol in symbols:
    url = baseurl + symbol
    print(url)
    data = requests.get(url, timeout=None).text
    print(data)