import sqlite3
import requests
import json
from datetime import datetime

dataset = list()
url = 'https://www.quandl.com/api/v3/datasets/BSE/BOM504067.json?api_key=fKXsYh9Qi9ySbS8X6pNh'
data = requests.get(url).text
mydataset = json.loads(data)
for row in mydataset['dataset']["data"]:
        tradedate = year = datetime.strptime(row[0], '%Y-%m-%d')
        open = float(row[1])
        close = float(row[4])
        dataset.append({'tradeDate':tradedate, 'open':open, 'close':close})

try:
    with sqlite3.connect('quandl') as db:
        cursor = db.cursor()  # this will create a cursor object

        # dynamic query using biding
        sql = '''insert into zensar values(:tradeDate,:open, :close)'''
        cursor.executemany(sql, dataset)
        db.commit()  # Only for DML queries
except Exception as E:
    print('Error: ', E)
else:
    print("DataBase table emp inserted with records!")
