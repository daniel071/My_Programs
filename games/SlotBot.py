# By Daniel Pavela 2018
# All source code is free as long as you credit me

# TODO: Use rethinkdb to make an online database for this.
# TODO: Fix up broad try and excepts
# TODO: Add update password system - Add email verification when changing password - with code

import time
from random import *
import sqlite3
import hashlib
import binascii
import os

loggedInUser = "0"


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


conn = sqlite3.connect('slotbot_users.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS accounts(user TEXT, password TEXT, points INT)')
conn.commit()


def save_points():
    global balance
    global loggedInUser

    if not loggedInUser == "0":
        c.execute('UPDATE accounts SET points = (?) WHERE user = (?)', [balance, loggedInUser])


def load_points():
    global balance
    global loggedInUser

    if not loggedInUser == "0":
        c.execute("SELECT * FROM accounts")
        accountInfo = c.fetchall()

        for row in accountInfo:
            if row[0] == loggedInUser:
                new_balance = row[2]
                # print("Account '{accountname} is same as logged in. "
                #       "Balance of this account is '{accountbalance}' \n".format(accountname=row[0],
                #       accountbalance=row[2]))
            else:
                pass
                # print("Account '{accountname} is not same as logged in. "
                #       "Balance of this account is '{accountbalance}'".format(accountname=row[0],
                #       accountbalance=row[2]))
        print("NEW BALANCE:", new_balance)
        balance = new_balance


def log_out():
    global loggedInUser
    global balance
    print("Signing out of account...")
    save_points()
    balance = 100.5
    loggedInUser = "0"
    print("Logged out of account!")
    print(
        "Balance reset to '100.5'\nTo restore your balance, "
        "log to your account again.")


balance = 100.5

first_loop = 1
while first_loop:
    ussr_input = input("Welcome! Do you have an account? (y/n) ").lower()
    if ussr_input == "y":
        permissionLoop = 1
        while permissionLoop == 1:
            # Ask for user
            userCheck = input("Input Username ")
            idLoop = 1
            idE = 0
            c.execute('SELECT * FROM accounts')
            accountInfo = c.fetchall()
            try:
                while idLoop == 1:
                    if accountInfo[idE][0] == userCheck:
                        idLoop = 0
                        # Ask for password
                        passwordCheck = input("Input password ")
                        currentState = verify_password(accountInfo[idE][1], passwordCheck)
                        if currentState is True:
                            print("Access Granted!")
                            loggedInUser = userCheck
                            balance = accountInfo[idE][2]
                            loggedInUser = str(loggedInUser)
                            load_points()
                            permissionLoop = 0
                            first_loop = 0
                        else:
                            print("Incorrect password. Access denied")
                    else:
                        idE = idE + 1
            except:
                print("No user '", userCheck, "' was found")

    elif ussr_input == "n":
        print("Continuing as guest, if you would like to create an account, use '/myaccount'")
        time.sleep(1)
        first_loop = 0
    else:
        print("Please type either y or n")
n = 1
n1 = 2
n2 = 1

while n == 1:
    commandInput = input("Please enter a command ")
    if commandInput == "/help":
        print("Use /balance to see your balance")
        print("Use /flipCoin to flip a coin")
        print("Use /rollDice to roll a dice")
        print("Use /luckyNumber to pick a number between 1 and 100")
        print("Use /shutdown to close the program")
        print("Use /credits to see who created this game and more info")
        print("Use /myaccount to create or login to your account and save your data")
    else:
        if commandInput == "/balance":
            print("Your balance is $", balance)
        else:
            if commandInput == "/flipCoin":
                n1 = 2
                while n1 == 2:
                    inputAnswer = input("Heads or Tails? [h / t] ")
                    if inputAnswer == "h":
                        print("You picked heads")
                    else:
                        if inputAnswer == "t":
                            print("You picked tails")
                        else:
                            print("Please either use [h / t]")
                            n1 = 1
                    moneyBet = int(input("How much money do you bet? "))
                    if balance < moneyBet:
                        print("You need $", moneyBet - balance, "more to bet that amount")
                    else:
                        coin = randint(1, 2)
                        if coin == 1:
                            coin = "h"
                        else:
                            coin = "t"
                        if coin == 1:
                            if coin == inputAnswer == "h":
                                print("Heads, you win!")
                                time.sleep(1)
                                balance = balance + moneyBet
                                save_points()
                                print("Your balance is now", balance)
                            else:
                                print("Tails, you lose!")
                                time.sleep(1)
                                balance = balance - moneyBet
                                save_points()
                                print("Your balance is now", balance)
                        else:
                            if coin == inputAnswer == "t":
                                print("Tails, you win!")
                                balance = balance + moneyBet
                                save_points()
                                time.sleep(1)
                                print("Your balance is now", balance)
                            else:
                                print("Heads, you lose!")
                                balance = balance - moneyBet
                                save_points()
                                time.sleep(1)
                                print("Your balance is now", balance)
                    n1 = 1
                    save_points()

            else:
                if commandInput == "/rollDice":
                    while n2 == 1:
                        try:
                            inputAnswer = int(input("Pick a number from 1 to 6 "))
                            if 0 > inputAnswer < 7:
                                moneyBet = int(input("How much money do you bet? "))
                                if balance < moneyBet:
                                    print("You need $", moneyBet - balance, "more to bet that amount")
                                else:
                                    diceNumber = randint(1, 6)
                                    if inputAnswer == diceNumber:
                                        print("The dice rolled a", diceNumber, "and you chose",
                                              inputAnswer, ",Congratulations!")
                                        time.sleep(1)
                                        balance = balance + moneyBet
                                        save_points()
                                        print("Your balance is now", balance)
                                        n2 = 0

                                    else:
                                        print("The dice rolled a", diceNumber, "and you chose",
                                              inputAnswer, "Sorry, maybe next time")
                                        balance = balance - moneyBet / 6
                                        save_points()
                                        print("Your balance is now", balance)
                                        n2 = 0
                            else:
                                print("Please pick a number from 1 to 6!")
                        except:
                            print("Please use an integer!")
                else:
                    if commandInput == "/shutdown":
                        save_points()
                        n = 0
                    else:
                        if commandInput == "/luckyNumber":
                            inputAnswer = int(input("Pick a number from 1 to 100 "))
                            print("$10 of your balance will be taken but if you get the lucky number,")
                            print("you will get $1500 back")
                            userAnswer = input("Are you sure you want to do this? [y / n]\n".lower())
                            if userAnswer == "y":
                                if balance < 11:
                                    print("Sorry, but you need", 10 - balance, "more dollars to make this purchase!")
                                else:
                                    balance = balance - 10
                                    save_points()
                                    save_points()
                                    if 0 > inputAnswer < 101:
                                        luckyNumber = randint(1, 100)
                                        if luckyNumber == userAnswer:
                                            balance = balance + 1500
                                            save_points()
                                            print("The lucky number was", luckyNumber,
                                                  "and your number was", inputAnswer, "Congratulations!")
                                            time.sleep(1)
                                            print("Congratulations! You picked the lucky number, your balance is now",
                                                  balance)
                                        else:
                                            print("The lucky number was", luckyNumber, "and your number was",
                                                  inputAnswer, "sorry!")
                                            time.sleep(1)
                                            print("Sorry, you didn't pick the lucky number, your balance is now",
                                                  balance)
                            else:
                                if userAnswer == "n":
                                    print("Sure!")
                                else:
                                    print("Please either answer y or n")

                        else:
                            if commandInput == "/credits":
                                print("SlotBot is a chance game created by")
                                print("Daniel Pavela, 2018")
                                print("All source code is free to use as long as you credit me")
                            else:
                                if commandInput == "/myaccount":
                                    my_account_loop = 1
                                    while my_account_loop:
                                        print("Please input an user config command")
                                        ussr_input = input("").lower()
                                        if ussr_input == "/help":
                                            print("Use /help to get this message\n"
                                                  "Use /signup to create a new account\n"
                                                  "Use /login to login to an existing account\n"
                                                  "Use /signout to signout of an existing account\n"
                                                  "Use /username to view your account name"
                                                  "Use /save to save you balance! (Not required as it does auto-save"
                                                  "Use /changepass to change your password (Work in progress)"
                                                  "Use /exit to exit this menu and return to the game\n")

                                        elif ussr_input == "/signup":
                                            addAccountLoop = 1
                                            while addAccountLoop == 1:
                                                user = input("Specify account name ")
                                                password = input("Specify account password ")
                                                hashedPass = hash_password(password)
                                                addAccountLoop = 0
                                                c.execute("INSERT INTO accounts (user, password, points) "
                                                          "VALUES (?, ?, ?)",
                                                          (user, hashedPass, balance))
                                                conn.commit()
                                                print("Use added successfully! "
                                                      "To log in to your new account, use /login")

                                        elif ussr_input == "/login":
                                            permissionLoop = 1
                                            while permissionLoop == 1:
                                                # Ask for user
                                                userCheck = input("Input Username ")
                                                idLoop = 1
                                                idE = 0
                                                c.execute('SELECT * FROM accounts')
                                                accountInfo = c.fetchall()
                                                try:
                                                    while idLoop == 1:
                                                        if accountInfo[idE][0] == userCheck:
                                                            idLoop = 0
                                                            # Ask for password
                                                            passwordCheck = input("Input password ")
                                                            currentState = verify_password(accountInfo[idE][1],
                                                                                           passwordCheck)
                                                            if currentState is True:
                                                                print("Access Granted!")
                                                                loggedInUser = userCheck
                                                                balance = accountInfo[idE][2]
                                                                loggedInUser = str(loggedInUser)
                                                                permissionLoop = 0
                                                                first_loop = 0
                                                                load_points()
                                                            else:
                                                                print("Incorrect password. Access denied")
                                                        else:
                                                            idE = idE + 1
                                                except:
                                                    print("No user '", userCheck, "' was found")

                                        elif ussr_input == "/exit":
                                            print(
                                                "Exiting out of account configurations.")
                                            time.sleep(1)
                                            my_account_loop = 0
                                        elif ussr_input == "/signout":
                                            log_out()

                                        elif ussr_input == "/username":
                                            if not loggedInUser == "0":
                                                print("Your account is '{accountname}'".format(accountname=loggedInUser
                                                                                               ))
                                            else:
                                                print("You are not logged in!")
                                        elif ussr_input == "/closeaccount":
                                            print("Are you sure you want to close your account? (y/n)")
                                            ussr_input = input("").lower()
                                            if ussr_input == "n":
                                                # User will say no and then get deleted MUHAHAHAHAHAHAHAHAHA
                                                # I'm nice ;) -- This is probably not a good idea...
                                                # I will change this later, only for testing




                                                if not loggedInUser == "0":
                                                    print("Deleting account '{accountname}' in "
                                                          "progress...".format(accountname=loggedInUser))
                                                    c.execute("DELETE FROM accounts WHERE user = (?)", (loggedInUser,))
                                                    conn.commit()
                                                    log_out()
                                                    print("User deleted successfully!")

                                                else:
                                                    print("You are not logged in!")
                                            elif ussr_input == "y":
                                                print("Returning to config page")
                                            else:
                                                print("Please use either (y/n)! Returning to config page.")
                                        elif ussr_input == "/save":
                                            print("Saving in progress...")
                                            save_points()
                                            print("Save successful!")
                                        elif ussr_input == "/changepass":
                                            # Work in progress
                                            pass
                                        else:
                                            print("Command not recognised, you can use /help")
                                else:
                                    print("Please enter a valid command, if you are unsure, type /help")
    float(balance)
    round(balance, 2)
    n2 = 1
