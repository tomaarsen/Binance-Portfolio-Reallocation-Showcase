# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:20:36 2018

@author: Cubie | Tom Aarsen
"""

import requests, time, random, math
import pandas as pd
import matplotlib.pyplot as p

class Crypto:
    def __init__(self, symbol):
        self.symbol = symbol
        self.close = []
        self.value = [1]
        self.amount = [1]
        print("Symbol:",symbol)
    
    # Fetch Historical data, store it, and return the length of the close list
    def FetchData(self, timeframe):
        url = "https://api.binance.com/api/v1/klines?interval={}&limit=1000&symbol={}".format(timeframe,self.symbol+"BTC")
        jsonDataList = FetchData(url).json()
        for jsonData in jsonDataList:
            self.close.append(float(jsonData[4]))
        return len(self.close)
	
    # Generate a Sine Wave or an inverted Sine Wave to fill Close. Also return length of close.
    def WaveData(self, t):
        if t == 0:
            for i in range(200):
                self.close.append(math.sin(math.pi * 30 * (i / 200) )+2)
        else:
            for i in range(200):
                self.close.append(-math.sin(math.pi * 30 * ( i / 200))+2)
        return len(self.close)

# Fetches data using URL
def FetchData(url):
    for i in range(20):
        try:
            jsonData = requests.get(url)
            return jsonData
        except:
            print("Sleeping due to Connection refusal")
            time.sleep(0.2)
    # ValueError only happens if the request fails 20 times in a row
    raise ValueError('Index > 20.')

def Main():
    # cryptoList will be a list of crypto class objects, each holding data of a specific coin
    cryptoList = []
    
    # Edit this variable to change the amount of randomly picked coins that the script uses.
    randomCoinAmount = 3
    
    # Edit this timeframe to change what timeframe the bot works with.
    timeframe = "6h"
    
    # Fill in the symbols you want to check in symbolList like this:
    # symbolList = ['ETH', 'XRP', 'EOS']
    symbolList = []
    for i in symbolList:
        cryptoList.append(Crypto(i))
    
    # If no specific symbols were requested:
    if(len(symbolList) == 0):
        # Get all coins listed on Binance
        data = FetchData('https://www.binance.com/exchange/public/product').json()['data']
        dataList = []
        for x, d in enumerate(data):
            if d['quoteAsset'] == "BTC":
                dataList.append(d)
        # Randomly pick a certain amount of coins. 
        randList = []
        while (len(cryptoList) < randomCoinAmount):
            rand = random.randint(0,len(dataList))
            if rand not in randList:
                cryptoList.append(Crypto(dataList[rand]['baseAsset']))
                randList.append(rand)
    
    # Fetching historical data for the coins
    lengthList = []
    for x, i in enumerate(cryptoList):
        lengthList.append(i.FetchData(timeframe))
        
        # You can comment the line above this and uncomment
        # the line below this, to have it generate a 
        # Sine wave pattern instead. a Sine pattern
        # on one coin with an inverted Sine pattern on another
        # gives the optimal performance of the bot
        
        #lengthList.append(i.WaveData(x))
    
    # Reducing length of the close data to be the size of the smallest
    # in the group of coins.
    for x, i in enumerate(cryptoList):
        i.close = i.close[-min(lengthList):]
	
    # Iterating over the length of the historical data stored
    for x in range(min(lengthList)):
        # Ignore 0 because at index 0 there is no "Previous close"
        if x == 0:
            continue
        
        # The val variable keeps track of the total value
        val = 0
        for i in cryptoList:
            # Value = amount dedicated to this coin * difference between current close and previous close
            i.value.append(i.amount[x-1] * (i.close[x]  / i.close[x-1]))
            val += i.value[-1]
			   
        for i in cryptoList:
            fee = 0
            # Use val variable to calculate average value
            average = val / len(cryptoList)
            # Calculate fee of the reallocation using current-day Binance
            # Fees with BNB. (0.01% per tx)
            if(i.amount[-1] < average):
                fee = ((val / len(cryptoList)) - i.amount[-1]) * 0.001
            # Amount keeps track of the relative amount dedicated to the coin
            i.amount.append(average - fee)
    
    # Create Pandas DataFrame to use for plotting
    df = pd.DataFrame({})
    
    maxList = []
    for i in cryptoList:
        # Filling DataFrame with Close and Value data of all coins
        df["Value of "+i.symbol] = i.value
        df["Close of "+i.symbol] = i.close
        
        # Keep track of the highest value of the close of each coin
        maxList.append(max(i.close))
    
    # Keylist will keep track of all columns in the DataFrame that will be plotted
    keyList = []
    
    # Adding Value (Performance with bot) and Base (Performance without bot)
    keyList.append("Performance with Bot")
    keyList.append("Performance without Bot")
    
    for i in cryptoList:
        key = 'Close of '+ i.symbol
        # Adjust the Close Column of each coin to start at value 1
        df[key] = df[key] * (1 / df[key].iloc[0])
        # Adding the Close of each coin to be plotted
        # Comment out the next line to prevent the Close for each coin
        # to be plotted.
        keyList.append(key)
    
    # Calculate Value and Base between the coins
    df["Performance with Bot"] = df["Value of "+cryptoList[0].symbol]
    df["Performance without Bot"] = df["Close of "+cryptoList[0].symbol]
    for x, i in enumerate(cryptoList):
        if x == 0:
            continue
        df["Performance with Bot"] += df["Value of "+i.symbol]
        df["Performance without Bot"] += df["Close of "+i.symbol]
    
    df["Performance with Bot"] = df["Performance with Bot"] / len(cryptoList)
    df["Performance without Bot"] = df["Performance without Bot"] / len(cryptoList)
    
    # Plotting the data
    df[keyList].plot(figsize=(10,5))
    p.title("Reallocation Bot Performance")
    p.show()
    
    # Printing data about Performance
    print("Final Gains with Bot    : {:.2f}x".format(df['Performance with Bot'].iloc[-1]))
    print("Final Gains without Bot : {:.2f}x".format(df['Performance without Bot'].iloc[-1]))
    
if __name__ == "__main__":
	Main()
