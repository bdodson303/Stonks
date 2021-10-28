def createAccount():
    import sql
    import stockMenu
    badUsernameLoopExitFlag = 0
    # This is the creating account menu
    while badUsernameLoopExitFlag == 0:
        username_ = input('please input username')
        usernameList = sql.getAllUsernames()
        betterUsernameList = stockMenu.fixWeirdSQLFormatedList(usernameList)
        if username_ not in betterUsernameList:
            badUsernameLoopExitFlag = 1
        else:
            print('This username is already being used')
    password_ = input('please input password')
    firstname_ = input('please input first name')
    lastname_ = input('please input last name')
    sql.createAccount(username_, password_, firstname_, lastname_)
    return username_