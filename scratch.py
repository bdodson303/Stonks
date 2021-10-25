
from colorama import init,Fore, Back, Style
init()
import random
import requests
import time
import math
from bs4 import BeautifulSoup
quoteDay = 0
sleepyTime = 1
AMDPRICEPAID = 109.90
FORDPRICEPAID=13.8012*4
INTELPRICEPAID=54.3046
MONSTERPRICEPAID=95.422
CRSRPRICEPAID=28.9194*4
TSMPRICEPAID=123.81
SANPRICEPAID=3.6371*2
MUXPRICEPAID=1.0493*2
TOTALINVESTMENT=AMDPRICEPAID+FORDPRICEPAID+INTELPRICEPAID+MONSTERPRICEPAID+CRSRPRICEPAID+TSMPRICEPAID+MUXPRICEPAID+SANPRICEPAID
class stock:
    def __init__(self,pricePaid,ticker,coName,yahooUrl,numberOfShares):
        self.numberOfShares = numberOfShares
        self.pricePaid = pricePaid
        self.ticker = ticker
        self.coName = coName
        self.yahooUrl = yahooUrl
        Source = requests.get(self.yahooUrl).text
        Soup = BeautifulSoup(Source, 'lxml')
        openPriceHtml = Soup.find("div", id="quote-summary")
        rawOpenPrice = openPriceHtml.div.table.tbody.find("span", class_="Trsdu(0.3s)").text
        self.openPrice = float(rawOpenPrice.replace(',',''))

        currentPriceHtml = Soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        self.currentPrice = float(currentPriceHtml.text.replace(',',''))

        self.daysChange = self.currentPrice - self.openPrice
        self.currentStockValue = self.currentPrice * self.numberOfShares

        self.daysChangeOnAccount = self.daysChange * self.numberOfShares

        self.daysChangePercent = (self.daysChange / self.openPrice) * 100

        self.moneyMadeOnStock = self.currentStockValue - self.pricePaid

        self.openPriceAccountValue = self.numberOfShares * self.openPrice
    def getStockPrice(self):
        #this attribute returns the stock price
        return self.currentPrice
    def getStockValue(self):
        #this attribute returns the stock price multiplied by the number of shares owned
        return self.currentStockValue
    def getDaysChange(self):
        return self.daysChange
    def getDaysChangeOnAccount(self):
        #this returns the ammount of money the stock has made us today
        return self.daysChangeOnAccount
    def getDaysChangePercent(self):
        return self.daysChangePercent
    def getMoneyMadeOnStock(self):
        return self.moneyMadeOnStock

    def getOpenPriceAccountValue(self):
        return self.openPriceAccountValue
    def getTicker(self):
        return self.ticker
    def getName(self):
        return self.coName
def getColor(value):
    if value < 0:
        return Fore.RED
    if value >= 0:
        return Fore.GREEN
def getColorWithGainLoss(value):
    if value < 0:
        return 'Loss Of' + Fore.RED
    if value >= 0:
        return 'Gain Of' + Fore.GREEN

while True:
    nasdaq = stock(0,'^ixic','NASDAQ','https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch',0)
    dow = stock(0,'^DJI','Dow Jones Industrial Average','https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI',0)
    amd = stock(AMDPRICEPAID,'AMD','Advanced Micro Devices',"https://finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch",1)
    ford = stock(FORDPRICEPAID,'F','Ford',"https://finance.yahoo.com/quote/F?p=F&.tsrc=fin-srch",4)
    intel = stock(INTELPRICEPAID,'INTC','Intel','https://finance.yahoo.com/quote/INTC?p=INTC&.tsrc=fin-srch',1)
    monster = stock(MONSTERPRICEPAID,'MNST','Monster','https://finance.yahoo.com/quote/MNST?p=MNST&.tsrc=fin-srch',1)
    corsair = stock(CRSRPRICEPAID,'CRSR','Corsair','https://finance.yahoo.com/quote/CRSR?p=CRSR&.tsrc=fin-srch',4)
    tsm = stock(TSMPRICEPAID,'TSM','Taiwan Semi-Conductor','https://finance.yahoo.com/quote/TSM?p=TSM&.tsrc=fin-srch',1)
    san = stock(SANPRICEPAID,'SAN','Banco Santander, S.A.','https://finance.yahoo.com/quote/SAN?p=SAN&.tsrc=fin-srch',2)
    mux = stock(MUXPRICEPAID,'MUX','McEwen Mining Inc.','https://finance.yahoo.com/quote/MUX?p=MUX&.tsrc=fin-srch',2)
    #initializes Stock Objects


    currentAccountValue = amd.getStockValue() + ford.getStockValue() + intel.getStockValue() + monster.getStockValue() + corsair.getStockValue() + tsm.getStockValue() + san.getStockValue() + mux.getStockValue()

    accountDaysChange = amd.getDaysChangeOnAccount() + ford.getDaysChangeOnAccount() + intel.getDaysChangeOnAccount() + monster.getDaysChangeOnAccount() + corsair.getDaysChangeOnAccount() + tsm.getDaysChangeOnAccount() + san.getDaysChangeOnAccount() + mux.getDaysChangeOnAccount()
    accountOpenPrice = amd.getOpenPriceAccountValue() + ford.getOpenPriceAccountValue() + intel.getOpenPriceAccountValue() + monster.getOpenPriceAccountValue() + corsair.getOpenPriceAccountValue() + tsm.getOpenPriceAccountValue() + san.getOpenPriceAccountValue() + mux.getOpenPriceAccountValue()

    accountDaysChangePercent = (accountDaysChange/accountOpenPrice)*100
    totalAccountChange = currentAccountValue - TOTALINVESTMENT
    totalAccountChangePercent = (totalAccountChange / TOTALINVESTMENT) * 100
    #code for account value, change and ,change percent
    #loss or gain
    time_ = time.ctime()
    timeList = time_.split(' ')
    clockList = timeList[4].split(':')
    currentHour = int(clockList[0])
    dayOfTheMonth = timeList[3]
    #clock stuff

    quotes = open('Quotes.txt','r')
    count = 0
    randomnumb = random.randint(0,351)
    if dayOfTheMonth != quoteDay:
        quoteDay = dayOfTheMonth
        for line in quotes:
            count = count + 1
            if count == randomnumb:
                quoteOfTheDay = line
    def compareStockToAccount(stockName):
        if stockName.getDaysChangePercent() < accountDaysChangePercent:
            print(Fore.YELLOW + Style.DIM + 'Your account is currently out-performing ' ,stockName.getName(), ' Today', Fore.CYAN, stockName.getTicker() ,':',getColor(stockName.getDaysChangePercent()), round(stockName.getDaysChangePercent(), 2), '%', Fore.CYAN,' Your Account:', getColor(accountDaysChangePercent), round(accountDaysChangePercent, 2), '%')
        elif stockName.getDaysChangePercent() == accountDaysChangePercent:
            print(Fore.YELLOW + Style.DIM + 'Your account is currently performing the same as ' ,stockName.getName(), ' Today', Fore.CYAN,stockName.getTicker(),':', getColor(dow.getDaysChangePercent()), round(dow.getDaysChangePercent(), 2), '%', Fore.CYAN,' Your Account:', getColor(accountDaysChangePercent), round(accountDaysChangePercent, 2), '%')
        elif stockName.getDaysChangePercent() > accountDaysChangePercent:
            print(Fore.YELLOW + Style.DIM +  stockName.getName(), 'is currently out-performing your account Today', Fore.CYAN, 'DJI:',getColor(stockName.getDaysChangePercent()), round(stockName.getDaysChangePercent(), 2), '%', Fore.CYAN,' Your Account:', getColor(accountDaysChangePercent), round(accountDaysChangePercent, 2), '%')
    compareStockToAccount(dow)
    #quote of the day stuff
    daysChangeOnAccountRankingNames = [amd,ford,intel,monster,corsair,tsm,mux,san]
    daysChangeOnAccountRanking = [amd.getDaysChangeOnAccount(), ford.getDaysChangeOnAccount(),intel.getDaysChangeOnAccount(),monster.getDaysChangeOnAccount(),corsair.getDaysChangeOnAccount(),tsm.getDaysChangeOnAccount(),mux.getDaysChangeOnAccount(),san.getDaysChangeOnAccount(),]
    n = len(daysChangeOnAccountRanking)
    for i in range(n):
        for j in range(0, n - i - 1):
            if daysChangeOnAccountRanking[j] < daysChangeOnAccountRanking[j + 1]:
                daysChangeOnAccountRanking[j], daysChangeOnAccountRanking[j + 1] = daysChangeOnAccountRanking[j + 1], daysChangeOnAccountRanking[j]
                daysChangeOnAccountRankingNames[j], daysChangeOnAccountRankingNames[j + 1] = daysChangeOnAccountRankingNames[j + 1], daysChangeOnAccountRankingNames[j]
    #code for ranking stock performance

    #Bubble Sort
    x = Fore.MAGENTA
    print(Fore.LIGHTWHITE_EX + '----------------------------------------')
    print(Fore.MAGENTA + Style.BRIGHT + time.ctime())
    if currentHour > 3 and currentHour <= 12:
        print(Fore.CYAN + 'Good Morning Benjamin')
    elif currentHour > 12 and currentHour <= 19:
        print(Fore.YELLOW + 'Good Evening Benjamin')
    else:
        print(Fore.RED + 'Good Night Benjamin')
    time.sleep(sleepyTime)
    print(Fore.LIGHTCYAN_EX + quoteOfTheDay,Style.RESET_ALL)
    time.sleep(sleepyTime)
    print(Fore.LIGHTWHITE_EX + '----------------------------------------')
    print(Fore.MAGENTA + '-Bens Alt Portfolio-')
    print(Fore.LIGHTWHITE_EX + '----------------------------------------')
    print(Fore.LIGHTMAGENTA_EX + '-Bens Investments-')
    if dow.getDaysChangePercent() < accountDaysChangePercent:
        print(Fore.YELLOW + Style.DIM + 'Your account is currently out-performing the Dow Today',Fore.CYAN,'DJI:',getColor(dow.getDaysChangePercent()),round(dow.getDaysChangePercent(),2),'%',Fore.CYAN,' Your Account:',getColor(accountDaysChangePercent),round(accountDaysChangePercent,2),'%')
    elif dow.getDaysChangePercent() == accountDaysChangePercent:
        print(Fore.YELLOW + Style.DIM + 'Your account is currently performing the same as the dow Today',Fore.CYAN,'DJI:',getColor(dow.getDaysChangePercent()),round(dow.getDaysChangePercent(),2),'%',Fore.CYAN,' Your Account:',getColor(accountDaysChangePercent),round(accountDaysChangePercent,2),'%')
    elif dow.getDaysChangePercent() > accountDaysChangePercent:
        print(Fore.YELLOW + Style.DIM + 'The Dow is currently out-performing your account Today',Fore.CYAN,'DJI:',getColor(dow.getDaysChangePercent()),round(dow.getDaysChangePercent(),2),'%',Fore.CYAN,' Your Account:',getColor(accountDaysChangePercent),round(accountDaysChangePercent,2),'%')
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[0].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[0].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ",getColor(daysChangeOnAccountRankingNames[0].getDaysChangePercent()) , round(daysChangeOnAccountRankingNames[0].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[0].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[0].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[1].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[1].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[1].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[1].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[1].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[1].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[2].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[2].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[2].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[2].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[2].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[2].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[3].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[3].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[3].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[3].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[3].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[3].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[4].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[4].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[4].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[4].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[4].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[4].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[5].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[5].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[5].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[5].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[5].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[5].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[6].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[6].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[6].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[6].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[6].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[6].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    print(Fore.LIGHTMAGENTA_EX + daysChangeOnAccountRankingNames[7].ticker, Fore.LIGHTYELLOW_EX,"$", daysChangeOnAccountRankingNames[7].getStockPrice(), Fore.LIGHTWHITE_EX, "Days Change: ", getColor(daysChangeOnAccountRankingNames[7].getDaysChangePercent()), round(daysChangeOnAccountRankingNames[7].getDaysChangePercent(),2),'%', Fore.LIGHTWHITE_EX,'Total', getColorWithGainLoss(daysChangeOnAccountRankingNames[7].getMoneyMadeOnStock()), '$',round(daysChangeOnAccountRankingNames[7].getMoneyMadeOnStock(),2))
    time.sleep(sleepyTime)
    if totalAccountChange < 0:
        totalAccountChangeColor = Fore.RED
    elif totalAccountChange >= 0:
        totalAccountChangeColor = Fore.GREEN

    print(Fore.CYAN + 'Total Account Change: $', Fore.LIGHTWHITE_EX,totalAccountChangeColor,"$", round(totalAccountChange,2),Fore.CYAN,'Todays Account Change',getColorWithGainLoss(accountDaysChange),'$',round(accountDaysChange,2))
    time.sleep(sleepyTime)
    print(Fore.CYAN + "Total Account Change Percent:", Fore.LIGHTWHITE_EX,totalAccountChangeColor, round(totalAccountChangePercent,2),"%",Fore.CYAN,'Todays Account Change Percent',getColorWithGainLoss(accountDaysChangePercent),round(accountDaysChangePercent,2),'%')
    print(Fore.LIGHTWHITE_EX + "----------------------------------------")
    time.sleep(15)
