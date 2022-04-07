from operator import index
import pandas as pd
import numpy as np  
import yfinance as yf
import datetime as dt
import pandas_datareader as pdr

yf.pdr_override()

stock = input(
    "Enter a stock ticker symbol:")
print(stock)

# moving average for n days

ma = int(input("Choose the moving average window in days:"))
print(ma)

startyear = 2022
startmonth = 2
startday  = 2

date = dt.datetime(
    startyear,
    startmonth,
    startday)  

now = dt.datetime.now()

data = pdr.get_data_yahoo(
    stock, # nome da ação
    date,  # data de inicio
    now    # data de fim da análise
)

print(data)


smaString = "Sma_" + str(ma)

# criar uma coluna para media movel no data.frame, usando o iloc para selecionar a coluna que será feita a conta 

data[smaString] = data.iloc[:,4].rolling(window=ma).mean()

print(data) 

# para tirar as primeiras N observações (já que não vai valor associado a elas)

data = data.iloc[ma:]

print(data)

for i in data.index:
    if(data["Adj Close"][i]<data[smaString][i]):
        print("The price is lower")
    else: 
        print("The price is higher")

    




