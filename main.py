# Defining the imports
from bot import Bot

# Creating the Tic Tac Toe bot
bot = Bot()

# Asking the player if he wants to play against a computer or real player
player_or_comp = input("Would you like to play against a computer or player? Answer with 'P' or 'C' \n").title()

# Starting the game depending on the player decision
# If the player decided to play against another player
if player_or_comp == "P":
    bot.vs_player()
elif player_or_comp == "C":
    bot.vs_comp()
else:
    print("Please select a valid option!")