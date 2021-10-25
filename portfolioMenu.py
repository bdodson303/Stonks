
def portfolioMenu(USERNAME):
    portfolioLoopExitFlag = 0
    import sql
    import stockMenu
    import usefullFunctions
    while portfolioLoopExitFlag == 0:
        portfolioNameLoopExitFlag = 0
        errorMenuOption = 0

        print("Portfolio Menu Options")
        print("1: Create Portfolio ")
        print("2: Open a current Portfolio")
        print("3: Delete a portfolio")
        print('4: Exit Program')
        userMenuOption = input()
        if userMenuOption == '1':
            while portfolioNameLoopExitFlag == 0:
                #this loop loops
                portfolioName = input('Portfolio Name:')
                portfolioId = USERNAME + '-' + portfolioName
                getPortfolio = sql.getPortfolio(portfolioId)
                if getPortfolio == None:
                    sql.createPortfollio(USERNAME, portfolioName, portfolioId)
                    print('Portfolio :', portfolioName, ' created')
                    stockMenu.stockMenu(portfolioId,portfolioName)
                    portfolioNameLoopExitFlag = 1
                else:
                    print('ERROR: portfollio has already been created Menu Options 1: re-enter name 2: exit')
                errorMenuOption = input()
                if errorMenuOption == '2':
                    portfolioNameLoopExitFlag = 1
                #checked 10/12/21
        elif userMenuOption == '2':
            portfolioCounter = 0
            formatedUserPortfolioList = []
            userPortfolioList = sql.getAllUserPortfolios(USERNAME)
            incorrectPortfolioNameLoopExitFlag = 0
            if len(userPortfolioList) > 0:
                while incorrectPortfolioNameLoopExitFlag == 0:
                    print('your current portfolios are:')
                    #this code below just prints a list of the current portfolios
                    for portfolioName in userPortfolioList:
                        portfolioCounter = portfolioCounter + 1
                        formatedUserPortfolioList.append(portfolioName[0])
                        print(portfolioCounter,': ',portfolioName[0])

                    portfolioName = input('please enter the name of the portfolio you would like to open:')
                    if portfolioName in formatedUserPortfolioList:
                        portfolioId = USERNAME + '-' + portfolioName
                        stockMenu.stockMenu(portfolioId,portfolioName)
                        incorrectPortfolioNameLoopExitFlag = 1
                    else:
                        print('Error ',portfolioName,' is not one of your portfolios')
                        print(' Menu Options')
                        print(' 1: Return to Portfolio Menu')
                        print(' 2: Exit to Portfolio Menu')
                        errorMenuOption = input()
                        if errorMenuOption == '2':
                            incorrectPortfolioNameLoopExitFlag = 1
            elif len(userPortfolioList) == 0:
                print('No Portfolios Currently In This Account')
        elif userMenuOption == '3':
            portfolioCounter_ = 0
            formatedUserPortfolioList_ = []
            userPortfolioList_ = sql.getAllUserPortfolios(USERNAME)
            deleteLoopExitFlag = 0
            if len(userPortfolioList_) > 0:
                while deleteLoopExitFlag == 0:
                    print('your current portfolios are:')
                    for portfolioName_ in userPortfolioList_:
                        portfolioCounter_ = portfolioCounter_ + 1
                        formatedUserPortfolioList_.append(portfolioName_[0])
                        print(portfolioCounter_,': ',portfolioName_[0])
                    portfolioName_ = input('please enter the name of the portfolio you would like to delete:')
                    if portfolioName_ in formatedUserPortfolioList_:
                        portfolioId_ = USERNAME + '-' + portfolioName_
                        print('Are you sure you want to delete portfolio:',portfolioName_)
                        print('1:yes')
                        print('2:no')
                        if input() == '1':
                            sql.deleteStockPortfolio(portfolioId_)
                            print('Portfolio',portfolioName_,'deleted')
                    else:
                        print('Error ',portfolioName_,' is not one of your portfolios')
                        print(' Menu Options')
                        print(' 1: Return to Portfolio Menu')
                        print(' 2: Enter another portfolio to be deleted')
                        errorMenuOption_ = input()
                        if errorMenuOption_ == '2':
                            deleteLoopExitFlag = 1
            elif len(userPortfolioList_) == 0:
                print('No Portfolios Currently In This Account')
        elif userMenuOption == '4':
            portfolioLoopExitFlag = 1
