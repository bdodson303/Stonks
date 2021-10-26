import requests
from tkinter import ttk
from bs4 import BeautifulSoup
import sql
from tkinter import *
from tkinter import messagebox
from ttkthemes import themed_tk as tk
from tkinter import ttk

def stockPage(portfolio,username):
    tkinterScroller = tk.ThemedTk()
    def refreshButtonClick():
        tkinterScroller.destroy()
        stockPage(portfolio,username)
    portfolioId = username+"-"+portfolio
    portfolioDataList= sql.getAllStockPortfolioData(portfolioId,'no')
    counter = 1
    for tist in portfolioDataList:
        print('hi')
        counter=counter+1
        stockTicker = tist[1]
        pricePaid = tist[2]
        numberOfShares = tist[3]
        stockData = sql.getStockData(stockTicker)
        coName = stockData[1]
        yahooUrl = stockData[2]

        Source = requests.get(yahooUrl).text
        Soup = BeautifulSoup(Source, 'lxml')
        openPriceHtml = Soup.find("div", id="quote-summary")
        rawOpenPrice = openPriceHtml.div.table.tbody.find("span", class_="Trsdu(0.3s)").text
        openPrice = float(rawOpenPrice.replace(',', ''))

        currentPriceHtml = Soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        currentPrice = float(currentPriceHtml.text.replace(',', ''))



        currPriceLabel = ttk.Label(tkinterScroller, text=currentPrice)
        currPriceLabel.grid(column=1, row=counter)

        #openPriceLabel = ttk.Label(tkinterScroller, text=openPrice)
        #openPriceLabel.grid(column=1, row=counter)

        stockTickerLabel = ttk.Label(tkinterScroller, text=stockTicker)
        stockTickerLabel.grid(column=0, row=counter)

    refreshButton = ttk.Button(tkinterScroller, text="Refresh", command=refreshButtonClick)
    portfolioName = ttk.Label(tkinterScroller, text=portfolio)
    portfolioName.grid(column="1", row="0", columnspan="2")
    refreshButton.grid(column="4", row="0")
    stockName = ttk.Label(tkinterScroller, text="Ticker", relief=RAISED)
    stockCurPrice = ttk.Label(tkinterScroller, text="Current Price", relief=RAISED)
    stockDaysChange = ttk.Label(tkinterScroller, text="Days Change", relief=RAISED)
    stockDaysChangeOnAccount = ttk.Label(tkinterScroller, text="Days Change /Account", relief=RAISED)
    stockCurPrice.grid(row=1, column=1,padx="5px")
    stockName.grid(row=1, column=0, padx="5px")
    stockDaysChange.grid(row=1, column=2,padx="5px")
    stockDaysChangeOnAccount.grid(row=1, column=3, padx="5px")
    tkinterScroller.mainloop()