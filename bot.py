# Defining the imports
import random as rand
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
logo = """
$$$$$$$$\ $$\                 $$$$$$$$\                           $$$$$$$$\                     
\__$$  __|\__|                \__$$  __|                          \__$$  __|                    
   $$ |   $$\  $$$$$$$\          $$ |    $$$$$$\   $$$$$$$\          $$ |    $$$$$$\   $$$$$$\  
   $$ |   $$ |$$  _____|         $$ |    \____$$\ $$  _____|         $$ |   $$  __$$\ $$  __$$\ 
   $$ |   $$ |$$ /               $$ |    $$$$$$$ |$$ /               $$ |   $$ /  $$ |$$$$$$$$ |
   $$ |   $$ |$$ |               $$ |   $$  __$$ |$$ |               $$ |   $$ |  $$ |$$   ____|
   $$ |   $$ |\$$$$$$$\          $$ |   \$$$$$$$ |\$$$$$$$\          $$ |   \$$$$$$  |\$$$$$$$\ 
   \__|   \__| \_______|         \__|    \_______| \_______|         \__|    \______/  \_______|                                                                                                                                                                                                                                                                                                
"""

# Creating the BOT class
class Bot:
    def __init__(self):
        # Creating the field
        row_1 = ["1", "◻", "◻", "◻"]
        row_2 = ["2", "◻", "◻", "◻"]
        row_3 = ["3", "◻", "◻", "◻"]
        header = ["0", "1", "2", "3"]
        self.field = [header, row_1, row_2, row_3]
        self.symbols = ["X", "O"]
        self.turns = 1

    # Creating the win conditions
    def check_win(self):
        if self.turns == 9:
            print("It's a draw!")
            return False
        elif self.field[1][1] == "X" and self.field[1][2] == "X" and self.field[1][3] == "X":
            print("Player X won!")
            return False
        elif self.field[2][1] == "X" and self.field[2][2] == "X" and self.field[2][3] == "X":
            print("Player X won!")
            return False
        elif self.field[3][1] == "X" and self.field[3][2] == "X" and self.field[3][3] == "X":
            print("Player X won!")
            return False
        elif self.field[1][1] == "X" and self.field[2][1] == "X" and self.field[3][1] == "X":
            print("Player X won!")
            return False
        elif self.field[1][2] == "X" and self.field[2][2] == "X" and self.field[3][2] == "X":
            print("Player X won!")
            return False
        elif self.field[1][3] == "X" and self.field[2][3] == "X" and self.field[3][3] == "X":
            print("Player X won!")
            return False
        elif self.field[1][1] == "X" and self.field[2][2] == "X" and self.field[3][3] == "X":
            print("Player X won!")
            return False
        elif self.field[1][3] == "X" and self.field[2][2] == "X" and self.field[3][1] == "X":
            print("Player X won!")
            return False
        elif self.field[1][1] == "O" and self.field[1][2] == "O" and self.field[1][3] == "O":
            print("Player O won!")
            return False
        elif self.field[2][1] == "O" and self.field[2][2] == "O" and self.field[2][3] == "O":
            print("Player O won!")
            return False
        elif self.field[3][1] == "O" and self.field[3][2] == "O" and self.field[3][3] == "O":
            print("Player O won!")
            return False
        elif self.field[1][1] == "O" and self.field[2][1] == "O" and self.field[3][1] == "O":
            print("Player O won!")
            return False
        elif self.field[1][2] == "O" and self.field[2][2] == "O" and self.field[3][2] == "O":
            print("Player O won!")
            return False
        elif self.field[1][3] == "O" and self.field[2][3] == "O" and self.field[3][3] == "O":
            print("Player O won!")
            return False
        elif self.field[1][1] == "O" and self.field[2][2] == "O" and self.field[3][3] == "O":
            print("Player O won!")
            return False
        elif self.field[1][3] == "O" and self.field[2][2] == "O" and self.field[3][1] == "O":
            print("Player O won!")
            return False
        else:
            return True

    # Restarting the game
    def restart(self, game_type):
        new_game = input("Would you like to play a new game? Y or N?").title()
        if new_game == "Y":
            self.turns = 1
            row_1 = ["1", "◻", "◻", "◻"]
            row_2 = ["2", "◻", "◻", "◻"]
            row_3 = ["3", "◻", "◻", "◻"]
            header = ["0", "1", "2", "3"]
            self.field = [header, row_1, row_2, row_3]
            if game_type == "comp":
                self.vs_comp()
            elif game_type == "player":
                self.vs_player()

    # Playing against a player
    def vs_player(self):
        win = True
        while win:
            clearConsole()
            print(logo)
            print(f"{self.field[0]}\n{self.field[1]}\n{self.field[2]}\n{self.field[3]}")
            coordinates = input("Please select a field to play! Ex 1,1:  ")
            coord_list = coordinates.split(",")
            if self.turns % 2 != 0:
                symbol = self.symbols[0]
            else:
                symbol = self.symbols[1]

            if self.field[int(coord_list[0])][int(coord_list[1])] == "◻":
                self.field[int(coord_list[0])][int(coord_list[1])] = symbol
                self.turns += 1
                win = self.check_win()
            else:
                print("You cannot play that field!")

        # Restarting the game
        self.restart("player")

    # Playing against the computer
    def vs_comp(self):
        win = True
        touples = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        while win:
            clearConsole()
            print(logo)
            print(f"{self.field[0]}\n{self.field[1]}\n{self.field[2]}\n{self.field[3]}")
            coordinates = input("Please select a field to play! Ex 1,1:  ")
            coord_list = coordinates.split(",")
            touple_item = (int(coord_list[0]), int(coord_list[1]))
            if self.field[int(coord_list[0])][int(coord_list[1])] == "◻":
                self.field[int(coord_list[0])][int(coord_list[1])] = "X"
                touples.remove(touple_item)
                self.turns += 1
                comp_choice = rand.choice(touples)
                self.field[comp_choice[0]][comp_choice[1]] = "O"
                touples.remove(comp_choice)
                self.turns += 1
                win = self.check_win()
            else:
                print("You cannot play that field!")

        # Restarting the game
        self.restart("comp")
