import sql
def getTickerList():
    tickerList = sql.getAllStockTickers()
    betterTickerList = []
    for ticker in tickerList:
        betterTickerList.append(ticker[0])
    return betterTickerList
def fixWeirdSQLFormatedList(weirdList):
    formatedList = []
    for item in weirdList:
        formatedList.append(item[0])
    return formatedList


def checkYahooUrl(yahooUrl):
    import requests
    from bs4 import BeautifulSoup
    try:
        Source = requests.get(yahooUrl).text
        Soup = BeautifulSoup(Source, 'lxml')
        openPriceHtml = Soup.find("div", id="quote-summary")
        rawOpenPrice = openPriceHtml.div.table.tbody.find("span", class_="Trsdu(0.3s)").text
        openPrice = float(rawOpenPrice.replace(',', ''))
        currentPriceHtml = Soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        currentPrice = float(currentPriceHtml.text.replace(',', ''))
        return 1
    except:
        return 0
def stockMenu(portfolioId,portfolioName):
    print('Stock Menu Options')
    print('1: Import Stock Into Portfolio')
    print('2: Import Stock Into Portfolio Watchlist')
    print('3: Delete stock from Portfolio')
    print('4: Exit to portfolioMenu')
    print('5: Exit Program')

    exitFlag = 0
    while exitFlag == 0:
        stockImportExitFlag = 0
        yahooChecker = 0
        tickerList = getTickerList()
        menuOption = input()
        print('Current Portfolio:', portfolioName)
        if menuOption == '1':
            watchlist = 'no'
            while stockImportExitFlag == 0:
                print('Please input the following data to Import Stock into portfolio:')
                print('ticker symbol')
                ticker = input()
                if ticker not in tickerList:
                    while yahooChecker == 0:
                        print('yahoo finance URL')
                        yahooUrl = input()
                        yahooChecker = checkYahooUrl(yahooUrl)
                        if yahooChecker == 1:
                            print('price paid for stock')
                            pricePaid = input()

                            print('company name:')
                            coName = input()
                            print('please enter the number of shares of ', coName, ' you own:')
                            numberOfShares = input()
                            sql.importStock(ticker, coName, yahooUrl)
                            sql.importStockPortfolioInfo(portfolioId, ticker, pricePaid, numberOfShares,watchlist)




                    else:
                        print("error with yahoo url you can 1: re-enter data 2: exit")
                        errorMenuOption = input()
                        if errorMenuOption == '2':
                            stockImportExitFlag = 1



                elif ticker in tickerList:
                    print('please enter the price you paid for',ticker)
                    pricePaid = input()
                    print('please enter the number Of Shares you own')
                    numberOfShares = input()
                    sql.importStockPortfolioInfo(portfolioId, ticker, pricePaid, numberOfShares, watchlist)
                print('Would you like to import another stock?')
                print('1:yes')
                print('2:no')
                if input() == '2':
                    stockImportExitFlag = 1
        elif menuOption == '2':
            watchlist = 'yes'
            while stockImportExitFlag == 0 and yahooChecker == 0:
                print('Please input the following data to Import Stock into portfolio watchlist:')
                print('ticker symbol')
                ticker = input()
                if ticker not in tickerList:

                    print('yahoo finance URL')
                    yahooUrl = input()
                    yahooChecker = checkYahooUrl(yahooUrl)
                    if yahooChecker == 1:
                        print('price paid for stock')
                        pricePaid = input()

                        print('company name:')
                        coName = input()
                        print('please enter the number of shares of ', coName, ' you own:')
                        numberOfShares = input()
                        sql.importStock(ticker, coName, yahooUrl)
                        sql.importStockPortfolioInfo(portfolioId, ticker, pricePaid, numberOfShares,watchlist)




                    else:
                        print("error with yahoo url you can 1: re-enter data 2: exit")
                        errorMenuOption = input()
                        if errorMenuOption == '2':
                            stockImportExitFlag = 1

        elif menuOption == '3':
            deleteStockTickerLoopExitFlag = 0
            while deleteStockTickerLoopExitFlag == 0:
                stockTickerToBeDeleted = input('please input the ticker of the stock that will be deleted from this portfolio')
                if stockTickerToBeDeleted in tickerList:
                    print('are you sure you want to delete ',stockTickerToBeDeleted,' 1:yes 2:no')
                    if input() == '1':
                        sql.deleteRowFromStockPortfolioTable(stockTickerToBeDeleted,portfolioId)
                        print(stockTickerToBeDeleted,' DELETED')
                        print('Would You Like To Delete Another? 1:yes 2:no')
                        deleteStockTickerMenuOption = input()
                        if deleteStockTickerMenuOption == '2':
                            deleteStockTickerLoopExitFlag = 1
                            exitFlag = 1
                            return 1
        elif menuOption == '4':
            exitFlag = 1
            return 1
        elif menuOption == '5':
            exitFlag = 1
            return 2










