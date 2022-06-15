from pickle import TRUE
from turtle import clear
import time
import os
from operator import truediv

from TicTacToe import TicTacToe


def dominik():  # RandomNumberGuesser

    import random
    randomNumber = random.randint(0, 100)
    win = False
    counter = 0
    while win == False:
        myGuessNumber = input("Geben Sie eine Zahl zwischen 0-100 ein: ")
        counter += 1

        try:
            int(myGuessNumber)
        except:
            continue

        if randomNumber == int(myGuessNumber):
            print("Du bist der Gewinner!!!")
            print("Du hast ", counter, " Versuche gebraucht.")
            win = True
            time.sleep(5)
            break
        else:
            if randomNumber < int(myGuessNumber):
                print("Deine Eingabe ist zu gross. Du musst eine kleinere Zahl eingeben!")
            else:
                print("Deine Eingabe ist zu klein. Du musst eine grössere Zahl eingeben!")


def vithu():  # TicTacToe
    x = TicTacToe()
    x.test()
    return

def fehlerMeldung():
    os.system('cls')
    print("\033[1;31;40m\n")
    print("Ein Fehler ist aufgetreten")
    time.sleep(1.5)
    print("\033[0;37;40m\n")
    os.system('cls')

# Main game:
while (True):
    os.system('cls')
    print(
        "Willkommen zu unserer kleinen Projektesammlung!\n" +
        "Tippen Sie die Zahl neben einem Projekt ein,\n" +
        "um das jeweilige Projekt anzuschauen:\n\n" +
        "(1) Tic Tac Toe\n" +
        "(2) Random Number Guesser\n" + 
        "(3) Beenden\n")

    try:
        userInput = int(input("Eingabe: "))
    except:
        fehlerMeldung()
        continue

    if (userInput == 1):
        vithu()
    elif (userInput == 2):
        dominik()
    elif (userInput == 3):
        exit()
    else:
        fehlerMeldung()
        continue