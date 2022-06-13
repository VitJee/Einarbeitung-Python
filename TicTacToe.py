from ast import AugStore
from cgitb import reset
import os
import time
from unittest import result


class TicTacToe:

    spielFeld = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))

    def test(self):
        os.system('cls')
        aktuellerSpieler = 'x'
        self.spielFeld = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))
        print("Geben Sie x ein um das Spiel zu beenden.\n")

        while (True):
            spielerWechsel = False
            print(
                "  1 2 3\n" +
                "A " + self.spielFeld[0] + "|" + self.spielFeld[1] + "|" + self.spielFeld[2] + "\n" +
                "  -+-+-\n" +
                "B " + self.spielFeld[3] + "|" + self.spielFeld[4] + "|" + self.spielFeld[5] + "\n" +
                "  -+-+-\n" +
                "C " + self.spielFeld[6] + "|" +
                self.spielFeld[7] + "|" + self.spielFeld[8] + "\n"
            )

            eingabe = str(input())

            if (eingabe == 'A1' or eingabe == 'a1'):
                if (self.spielFeld[0] == ' '):
                    self.spielFeld[0] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'A2' or eingabe == 'a2'):
                if (self.spielFeld[1] == ' '):
                    self.spielFeld[1] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'A3' or eingabe == 'a3'):
                if (self.spielFeld[2] == ' '):
                    self.spielFeld[2] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'B1' or eingabe == 'b1'):
                if (self.spielFeld[3] == ' '):
                    self.spielFeld[3] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'B2' or eingabe == 'b2'):
                if (self.spielFeld[4] == ' '):
                    self.spielFeld[4] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'B3' or eingabe == 'b3'):
                if (self.spielFeld[5] == ' '):
                    self.spielFeld[5] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'C1' or eingabe == 'c1'):
                if (self.spielFeld[6] == ' '):
                    self.spielFeld[6] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'C2' or eingabe == 'c2'):
                if (self.spielFeld[7] == ' '):
                    self.spielFeld[7] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'C3' or eingabe == 'c3'):
                if (self.spielFeld[8] == ' '):
                    self.spielFeld[8] = aktuellerSpieler
                    spielerWechsel = True
            elif (eingabe == 'X' or eingabe == 'x'):
                break

            if (spielerWechsel == True):
                if (aktuellerSpieler == 'x'):
                    aktuellerSpieler = 'o'
                else:
                    aktuellerSpieler = 'x'

            if (self.resultat() == 'x'):
                os.system('cls')
                print("Der Spieler x hat gewonnen!")
                time.sleep(1.5)
                break
            elif (self.resultat() == 'o'):
                os.system('cls')
                print("Der Spieler o hat gewonnen!")
                time.sleep(1.5)
                break
            elif (self.resultat() == 'a'):
                os.system('cls')
                print("Es ist unentschieden!")
                time.sleep(1.5)
                break
        pass

    def resultat(self):
        if (self.spielFeld[0] == self.spielFeld[1] and self.spielFeld[0] == self.spielFeld[2]):
            if (self.spielFeld[0] == 'x'):
                return 'x'
            elif (self.spielFeld[0] == 'o'):
                return 'o'
        elif (self.spielFeld[3] == self.spielFeld[4] and self.spielFeld[3] == self.spielFeld[5]):
            if (self.spielFeld[3] == 'x'):
                return 'x'
            elif (self.spielFeld[3] == 'o'):
                return 'o'
        elif (self.spielFeld[6] == self.spielFeld[7] and self.spielFeld[6] == self.spielFeld[8]):
            if (self.spielFeld[6] == 'x'):
                return 'x'
            elif (self.spielFeld[6] == 'o'):
                return 'o'
        elif (self.spielFeld[0] == self.spielFeld[4] and self.spielFeld[0] == self.spielFeld[8]):
            if (self.spielFeld[0] == 'x'):
                return 'x'
            elif (self.spielFeld[0] == 'o'):
                return 'o'
        elif (self.spielFeld[2] == self.spielFeld[4] and self.spielFeld[2] == self.spielFeld[6]):
            if (self.spielFeld[2] == 'x'):
                return 'x'
            elif (self.spielFeld[2] == 'o'):
                return 'o'
        elif (self.spielFeld[0] != ' ' and self.spielFeld[1] != ' ' and self.spielFeld[2] != ' ' and self.spielFeld[3] != ' ' and self.spielFeld[4] != ' ' and self.spielFeld[5] != ' ' and self.spielFeld[6] != ' ' and self.spielFeld[7] != ' ' and self.spielFeld[8] != ' '):
            return 'a'
        else:
            return ' '
