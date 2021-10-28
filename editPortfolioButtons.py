import sql
from tkinter import *
from tkinter import messagebox
from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter import messagebox
import yfinance as yf
def tickerCheck(ticker):
    test = yf.Ticker(ticker)
    print(test.info['regularMarketPrice'])
    if test.info['regularMarketPrice'] == None:
        return 0
    else:
        return 1
def addStockPage(portfolioId,stockTickerList):
    try:
        addStockPageTK = tk.ThemedTk()
        def addStockButtonClick():
            #sql.importStockPortfolioInfo()
            pricePaidInput = float(pricePaidObj.get())
            stockTickerInput = stockTickerObj.get()
            numberOfSharesInput = int(numberOfSharesObj.get())
            if tickerCheck(stockTickerObj.get()) == 1:
                if stockTickerInput not in stockTickerList:
                    sql.importStockPortfolioInfo(portfolioId,stockTickerInput,pricePaidInput,numberOfSharesInput,'no')
                    messagebox.showinfo('Success','Stock '+str(stockTickerInput)+' successfully imported')
                    addStockPageTK.destroy()
                else:
                    messagebox.showerror('Error','Stock '+str(stockTickerInput)+' already in portfolio' )
            else:
                messagebox.showerror("Ticker Error","Ticker regMarketPrice Returned None please re-enter")

        stockTickerLabel = ttk.Label(addStockPageTK,text='stock ticker:')
        stockTickerLabel.grid(row=1,column=0)
        pricePaidLabel = ttk.Label(addStockPageTK, text='Price you paid for stock:')
        pricePaidLabel.grid(row=2,column=0)
        numberOfSharesLabel=ttk.Label(addStockPageTK, text='Number of Shares You Own:')
        numberOfSharesLabel.grid(row=3,column=0)
        stockTickerObj = StringVar()
        pricePaidObj = StringVar()
        numberOfSharesObj = StringVar()

        stockTickerEntry = ttk.Entry(addStockPageTK,textvariable=stockTickerObj)
        pricePaidEntry= ttk.Entry(addStockPageTK,textvariable=pricePaidObj)
        numberOfSharesEntry = ttk.Entry(addStockPageTK,textvariable=numberOfSharesObj)
        addStockButton=Button(addStockPageTK,text='Add',command=addStockButtonClick)
        addStockButton.grid(row=4,column=1)
        pricePaidEntry.grid(row=2,column=1)
        stockTickerEntry.grid(row=1,column=1)
        numberOfSharesEntry.grid(row=3,column=1)
        addStockPageTK.mainloop()
    except:
        messagebox.showerror(ERROR,'error with entry please retry')
def deleteStockPage(portfolioId,stockTickerList):
    deleteStockPage = tk.ThemedTk()
    def deleteStockSubmitClick():
        deleteStockInput = deleteStockInputObj.get()
        if deleteStockInput in stockTickerList:
            sql.deleteRowFromStockPortfolioTable(deleteStockInputObj.get(),portfolioId,'no')
            messagebox.showinfo('success ','Stock '+deleteStockInput+' deleted')
            deleteStockPage.destroy()
        else:
            messagebox.showerror('ERROR','Ticker '+deleteStockInput+' not in portfolio')
    deleteStockLabel=Label(deleteStockPage,text='Please input Stock To Be Deleted:')
    deleteStockLabel.grid(row=1,column=0)
    deleteStockInputObj = StringVar()
    deleteStockInput = Entry(deleteStockPage,textvariable=deleteStockInputObj)
    deleteStockInput.grid(row=1,column=1)
    deleteStockSubmitButton = Button(deleteStockPage,command= deleteStockSubmitClick,text='Delete')
    deleteStockSubmitButton.grid(row=2,column=1)
    deleteStockPage.mainloop()

