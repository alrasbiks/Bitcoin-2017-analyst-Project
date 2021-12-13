# The purpose of this program is to create charts for bitcoin (closing) prices in the year of 2017
# specifically for the months of November and December along with comparing both months to January 2018
# and comparing 2016, 2017, and 2018 altogether.
############################################################################################################

import pandas as pd
import matplotlib.pyplot as plt

# Bitcoin closing price in 2016
df = pd.read_csv('BTC2016.csv')

df.plot(kind='scatter', x='Date', y='Closing Price (USD)', title='2016')

plt.show()

# Bitcoin closing price in 2017
df = pd.read_csv('BTC2017.csv')

df.plot(kind='scatter', x='Date', y='Closing Price (USD)', title='2017')

plt.show()

# Bitcoin closing price in 2018

df = pd.read_csv('BTC2018.csv')

df.plot(kind='scatter', x='Date', y='Closing Price (USD)', title='2018')

plt.show()

# Bitcoin closing price November 2017
df = pd.read_csv('November2017.csv')

df.plot(kind='line', x='Date', y='Closing Price (USD)', title='November 2017')

plt.show()

# Bitcoin closing price in December 2017
df = pd.read_csv('December17.csv')

df.plot(kind='line', x='Date', y='Closing Price (USD)', title='December 2017')

plt.show()

# Bitcoin closing price in January 2018
df = pd.read_csv('January2018.csv')

df.plot(kind='line', x='Date', y='Closing Price (USD)', title='January 2018')

plt.show()