# 3x3 Tic-Tac-Toe board
import os
tic_tac_toe_board = [
   [' ', ' ', ' '],
   [' ', ' ', ' '],
   [' ', ' ', ' ']
]
select=input("WITAJ W GRZE KÓŁKO I KRZYŻYK\nWpisz:\n1-Aby zacząć\n2-Poradnik\n")

if select=="1":
    znak=input("Wybierz swój znak:\nX-Zaczynasz\nO-Zaczyna komputer\n")
    if znak=="X":
        os.system('cls')
        print("Twój znak: X")
        pozycja=input("Twój ruch:")
        print("")
        
        # for row in tic_tac_toe_board:
        #     for column in row:
        #         print(column, end=" ")
        #     print("")