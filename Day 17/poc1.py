import sqlite3

try:
    with sqlite3.connect('quandl') as db:
        cursor = db.cursor()  # this will create a cursor object
        cursor.execute('create table zensar (tradeDate date, open float, \
                      close float)')
except Exception as E:
    print('Error: ', E)
else:
    print("DataBase table emp created successfully!")
