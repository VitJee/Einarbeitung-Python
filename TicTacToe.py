from ast import AugStore
import os


class TicTacToe:

    spielFeld = list((" ", " ", " ", " ", " ", " ", " ", " ", " "))

    def __init__(objekt):
        pass

    def test(objekt):
        os.system('cls')
        aktuellerSpieler = 'x'

        while (True):
            spielerWechsel = True
            print(
                "  A B C\n" +
                "1 " + objekt.spielFeld[0] + "|" + objekt.spielFeld[1] + "|" + objekt.spielFeld[2] + "\n" +
                "  -+-+-\n" +
                "2 " + objekt.spielFeld[3] + "|" + objekt.spielFeld[4] + "|" + objekt.spielFeld[5] + "\n" +
                "  -+-+-\n" +
                "3 " + objekt.spielFeld[6] + "|" +
                objekt.spielFeld[7] + "|" + objekt.spielFeld[8] + "\n"
            )

            eingabe = str(input())

            if (eingabe == 'A1' or eingabe == 'a1'):
                objekt.spielFeld[0] = aktuellerSpieler
            elif (eingabe == 'A2' or eingabe == 'a2'):
                pass
            elif (eingabe == 'A3' or eingabe == 'a3'):
                pass
            elif (eingabe == 'B1' or eingabe == 'b1'):
                pass
            elif (eingabe == 'B2' or eingabe == 'b2'):
                pass
            elif (eingabe == 'B3' or eingabe == 'b3'):
                pass
            elif (eingabe == 'C1' or eingabe == 'c1'):
                pass
            
            else:
                spielerWechsel = False

            if (spielerWechsel == True):
                if (aktuellerSpieler == 'x'):
                    aktuellerSpieler = 'o'
                else:
                    aktuellerSpieler = 'x'
            else:
                pass

        pass
