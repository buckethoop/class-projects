# This is a rock paper scissors game where you compete against the computer
import random


def start():
    # Allows player to input their move
    user = input("Choose 'r' for rock, 'p' for paper, or 's' for scissors: ")
    # Randomizes computer's move
    comp = random.choice(['r', 'p', 's'])

    if user == comp:
        return "It's a tie :|"

    if win(user, comp):
        return "You Win :)"

    else:
        return "You Lose :("

# Function that compares the moves of both the player and computer and determines a winner
def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True

print(start())

