import sqlite3
import sql
import Userlogin
import portfolioMenu
import pyfiglet
from colorama import Fore, Back, Style
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
result = pyfiglet.figlet_format("STONKS CO.")
print(Style.BRIGHT + Fore.GREEN + result)
print(Fore.LIGHTCYAN_EX + 'Login Menu Options')
print(Fore.LIGHTWHITE_EX+'1:',Fore.LIGHTYELLOW_EX + 'Login')
print(Fore.LIGHTWHITE_EX+'2:',Fore.LIGHTYELLOW_EX + 'Create Account')
menuoption = int(input())
if menuoption == 2:
    USERNAME = createAccount.createAccount()
    portfolioMenu.portfolioMenu(USERNAME)
elif menuoption == 1:
    USERNAME = Userlogin.userLogin()
    usersFirstName = sql.getUsersFirstName(USERNAME)
    print('Hello, ', usersFirstName[0])
if USERNAME != int(1):
    #if Username and password are able to be verified
    portfolioMenu.portfolioMenu(USERNAME)


    #if portfolioInfo != None:
        #screen users will see after they open a portfolio











