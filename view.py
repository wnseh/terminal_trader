#!/usr/bin/env python3

import os


def log_or_sign():
    os.system('clear')
#    os.system('cowsay "Welcome to Terminal Trader.\n" | lolcat')
    os.system('figlet Terminal Trader | lolcat -a -d 2')
    print('[l] Log in\n[c] Create a new account\n[e] Exit\n')
    return input(">MAIN> ")
#    answer = input("Welcome.Do you already have a userid?\n[y] Yes\n[n] No\n")
#    yes= ['y', 'yes']
#    no= ['n', 'no']
#    if answer in yes:
#        userid = input("What is your userid?\n")
#        password = input("What is your password?\n")
def log_menu():
    head()
    username = input("What is your username?\n")
    password = input("What is your password?\n")
    return username,password

def create_menu():
    head()
    a = input("Create an username:\n")
    b = input("Create a password:\n")
    c = input("How much money you will invest:\n")
    return a,b,c

def fund_menu():
    head()
    a = float(input("How much money would you like to fund to your account?:\n"))
    if a >= 0:
        return True, a
    else:
        return False, a

def head():
    os.system('clear')
    os.system('cowsay -f vader "Terminal Trader\n" | lolcat')

def main_menu():
    head()
    print('[f] Fund\n[b] Buy\n[s] Sell\n[l] Lookup\n[q] Quote\n[d] Display\n[e] Exit\n')
    #print('[b] Buy\n[s] Sell\n[l] Lookup\n[q] Quote\n[d] Display\n[e] Exit\n')
    return input(">MAIN> ")


def buy_menu():
    head()
    x = input('Ticker Symbol: ')
    y = float(input('Trade Volume: '))
    return x, y


def lookup_menu():
    head()
    return input('>MAIN>LOOKUP> ')


def quote_menu():
    head()
    return input('>MAIN>QUOTE> ')

def sell_menu():
    head()
    x = input('Ticker Symbol: ')
    y = float(input('Trade Volume: '))
    return x, y
