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
        myGuessNumber = input("Enter a random Number between 0-100: ")
        counter += 1
        
        if randomNumber == int(myGuessNumber):
            print("You are the winner!!!")
            print("You had needed ", counter, " moves.")
            win = True
            time.sleep(5)
            break
        else:
            if randomNumber < int(myGuessNumber):
                print("Your choose is to high. You must give a lower number!")
            else:
                print("Your choose is to low. You must give a higher number!")
        
                
def vithu():  # TicTacToe
    print("Vithu")
    return


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

    userInput = int(input("Eingabe: "))

    if (userInput == 1):
        x = TicTacToe()
        x.test()
    elif (userInput == 2):
        dominik()
    elif (userInput == 3):
        exit()
    else:
        os.system('cls')
        print("\033[1;31;40m\n")
        print("Ein Fehler ist aufgetreten")
        time.sleep(1.5)
        print("\033[0;37;40m\n")
        os.system('cls')
        continue
    continue