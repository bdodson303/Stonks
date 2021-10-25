import requests
import time
from bs4 import BeautifulSoup
amdPriceAtOpen = 100.92
fordPriceAtOpen = 14.44
intelPriceAtOpen = 53.55
monsterPriceAtOpen = 88.76
corsairPriceAtOpen = 25.65
tsmPriceAtOpen = 109.80
sanPriceAtOpen= 3.7300
muxPriceAtOpen = 1.0600
AMDPRICEPAID = 109.90
FORDPRICEPAID=13.8012*4
INTELPRICEPAID=54.3046
MONSTERPRICEPAID=95.422
CRSRPRICEPAID=28.9194*4
TSMPRICEPAID=123.81
SANPRICEPAID=3.6371*2
MUXPRICEPAID=1.0493*2
TOTALINVESTMENT=AMDPRICEPAID+FORDPRICEPAID+INTELPRICEPAID+MONSTERPRICEPAID+CRSRPRICEPAID+TSMPRICEPAID+MUXPRICEPAID+SANPRICEPAID
print(TOTALINVESTMENT)
while True:
    amdSource = requests.get('https://finance.yahoo.com/quote/AMD?p=AMD&.tsrc=fin-srch').text
    amdSoup = BeautifulSoup(amdSource, 'lxml')
    amdPriceHtml = amdSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentAmdPrice = float(amdPriceHtml.text)


    fordSource = requests.get('https://finance.yahoo.com/quote/F?p=F&.tsrc=fin-srch').text
    fordSoup = BeautifulSoup(fordSource, 'lxml')
    fordPriceHtml = fordSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentFordPrice = float(fordPriceHtml.text)


    intelSource = requests.get('https://finance.yahoo.com/quote/INTC?p=INTC&.tsrc=fin-srch').text
    intelSoup = BeautifulSoup(intelSource, 'lxml')
    intelPriceHtml = intelSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentIntelPrice = float(intelPriceHtml.text)


    monsterSource = requests.get('https://finance.yahoo.com/quote/MNST?p=MNST&.tsrc=fin-srch').text
    monsterSoup = BeautifulSoup(monsterSource, 'lxml')
    monsterPriceHtml = monsterSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentMonsterPrice = float(monsterPriceHtml.text)


    corsairSource = requests.get('https://finance.yahoo.com/quote/CRSR?p=CRSR&.tsrc=fin-srch').text
    corsairSoup = BeautifulSoup(corsairSource, 'lxml')
    corsairPriceHtml = corsairSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentCorsairPrice = float(corsairPriceHtml.text)


    tsmSource = requests.get('https://finance.yahoo.com/quote/TSM?p=TSM&.tsrc=fin-srch').text
    tsmSoup = BeautifulSoup(tsmSource, 'lxml')
    tsmPriceHtml = tsmSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentTsmPrice = float(tsmPriceHtml.text)


    muxSource = requests.get('https://finance.yahoo.com/quote/MUX?p=MUX&.tsrc=fin-srch').text
    muxSoup = BeautifulSoup(muxSource, 'lxml')
    muxPriceHtml = muxSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentMuxPrice = float(muxPriceHtml.text)


    sanSource = requests.get('https://finance.yahoo.com/quote/SAN?p=SAN&.tsrc=fin-srch').text
    sanSoup = BeautifulSoup(sanSource, 'lxml')
    sanPriceHtml = sanSoup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    currentSanPrice = float(sanPriceHtml.text)


    #This block of code here constantly updates the current stock prices
    amdInvestmentChange = currentAmdPrice - AMDPRICEPAID
    fordInvestmentChange = currentFordPrice - FORDPRICEPAID
    intelInvestmentChange = currentIntelPrice - INTELPRICEPAID
    monsterInvestmentChange = currentMonsterPrice - MONSTERPRICEPAID
    corsairInvestmentChange = currentCorsairPrice - CRSRPRICEPAID
    tsmInvestmentChange = currentTsmPrice - TSMPRICEPAID
    muxInvestmentChange = currentMuxPrice - MUXPRICEPAID
    sanInvestmentChange = currentSanPrice - SANPRICEPAID

    accountValue = currentAmdPrice + 4 * currentFordPrice + currentIntelPrice + currentMonsterPrice + 4 * currentCorsairPrice + currentTsmPrice + 2 * currentMuxPrice + 2 * currentSanPrice
    totalAccountChange = accountValue - TOTALINVESTMENT

    if totalAccountChange < 0:
        outputTotalAccountChange = "Loss of " + str(totalAccountChange)
    elif totalAccountChange >= 0:
        outputTotalAccountChange = "Gain of " + str(totalAccountChange)
    totalAccountChangePercent = (totalAccountChange / TOTALINVESTMENT)*100

    # this block calculates change on investment
    time_ = time.ctime()
    print(time_)
    timeList = time_.split(' ')
    clockList = timeList[4].split(':')
    currentHour = clockList[0]
    #some clock stuff
    if currentHour == "6":
        amdPriceAtOpen = currentAmdPrice
        fordPriceAtOpen = currentFordPrice
        intelPriceAtOpen = currentIntelPrice
        monsterPriceAtOpen = currentMonsterPrice
        corsairPriceAtOpen = currentCorsairPrice
        tsmPriceAtOpen = currentTsmPrice
        sanPriceAtOpen = currentSanPrice
        muxPriceAtOpen = currentMuxPrice
    if amdPriceAtOpen > 0:
        amdDaysPriceChange = currentAmdPrice - amdPriceAtOpen
        fordDaysPriceChange = currentFordPrice - fordPriceAtOpen
        intelDaysPriceChange = currentIntelPrice - intelPriceAtOpen
        monsterDaysPriceChange = currentMonsterPrice - monsterPriceAtOpen
        corsairDaysPriceChange = currentCorsairPrice - corsairPriceAtOpen
        tsmDaysPriceChange = currentTsmPrice - tsmPriceAtOpen
        sanDaysPriceChange = currentSanPrice - sanPriceAtOpen
        muxDaysPriceChange = currentMuxPrice - muxPriceAtOpen
    print('----------------------------------------')
    print("AMD", currentAmdPrice," change: ",amdDaysPriceChange)
    print("Ford", currentFordPrice," change: ",fordDaysPriceChange)
    print("Intel", currentIntelPrice," change: ",intelDaysPriceChange)
    print("Monster:", currentMonsterPrice," change: ",monsterDaysPriceChange)
    print("Corsair", currentCorsairPrice," change: ",corsairDaysPriceChange)
    print("Tsm", currentTsmPrice," change: ",tsmDaysPriceChange)
    print("Mux", currentMuxPrice," change: ",muxDaysPriceChange)
    print("san", currentSanPrice," change: ",sanDaysPriceChange)
    print('totalAccountChange:', totalAccountChange)
    print("totalAccountChangePercent:%", totalAccountChangePercent)
    print("----------------------------------------")
    time.sleep(15)
        #gotta be carfull with this section it collects the data for price at open in the morning so if its not open during this time things could get weird
