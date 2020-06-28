import pandas as pd
import quandl
import matplotlib.pyplot as plt

zensar = quandl.get("BSE/BOM504067",
                    authtoken="fKXsYh9Qi9ySbS8X6pNh",
                    start_date="1970-01-01", end_date="2020-01-01")
zensar['Date'] = pd.to_datetime(zensar.index)
zensar['year'] = zensar['Date'].dt.year
df1 = zensar[['year', 'Close']].groupby('year').mean()

# Plotting a line graph on zensar dataset
x = df1.index
years = df1.values
fig, ax = plt.subplots()
line1, = ax.plot(x, years, '--', linewidth=2,
                 label='Dashes set retroactively')
ax.legend(loc='lower right')
plt.grid()
plt.show()
#zensar = pd.read_csv('BSE-BOM504067.csv')
#zensar['year'] = pd.to_datetime(zensar.Date).dt.year
#print(zensar[['Close', 'year']].groupby('year').mean())

#print(zensar[zensar['year'] == 2019].Close.mean())
#print(zensar[['Date', 'Close', 'year']].head(10))