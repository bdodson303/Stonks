import sqlite3
import sql
import Userlogin
import portfolioMenu
import stockMenu
import createAccount
import requests
from bs4 import BeautifulSoup
inputedPassword = 0
exitFlag = 0
wrongPasswordCounter = 0
password = None
userMenuOption = 0
USERNAME = 1
mainMenuLoopExitFlag = 0
portfolioMenuLoop = 1
badUsernameLoop = 0
print('Login Menu Options')
print('1: Login')
print('2: Create Account')
menuoption = int(input())
if menuoption == 2:
    createAccount.createAccount()
elif menuoption == 1:
    USERNAME = Userlogin.userLogin()
    usersFirstName = sql.getUsersFirstName(USERNAME)
    print('Hello, ', usersFirstName[0])
if USERNAME != int(1):
    #if Username and password are able to be verified
    portfolioMenu.portfolioMenu(USERNAME)


    #if portfolioInfo != None:
        #screen users will see after they open a portfolio











