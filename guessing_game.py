'''
Author: acbart (2/6/2019)
Version: 1
Co-author: ___xinyi sun_____ (__702452389_____)

1. Give a brief description of how the code below works.
   Use plain, accessible language and avoid repeating
   the exact statements from the code. Aim to write at
   least 3 sentences.
   
   __In the main game parts,it stes up "print welcome".because
   this is the beginning of the game.Also, there is "pring ending" because you are win the game.______________________________
   ________________________________
   ________________________________

2. Make a modification to the code in some place that changes the game
   in some interesting way. This cannot be as simple as changing the
   MINIMUM or one of the printed messages, but make enough changes and
   they can add up. You might allow the player to play more rounds after
   the first one, or completely change all the messages to have a pirate
   theme, or make it so the player can specify the maximum number.
   Describe your change here clearly and explain why you thought it was
   interesting.
   
   _______I think it could be more clear  when the user guess the number. if you give a hint, user will quicly to gusee the correct one._______________________
   ________________________________
   ________________________________

'''

# Import the randint function generate random integers
from random import randint

# Establish the lower and uppper bound on the goal number
Lowest = 1
Highest= 10

def print_welcome():
    '''
    Prompt the user for their name, and then display a
    simple message explaining the rules of the game.
    '''
    # Get the name of the user
    name = input("What is your name? ")
    # Show the user's name
    print("Hello", name, "and welcome to my guessing game.")
    # Print out the limits of the goal number
    print("I've thought of a number between", Highest, "and", Lowest)
    # Write out rest of the instructions
    print("You need to guess that number.")
    print("I'll tell you if you need to go higher or lower.")
    
def print_ending():
    '''
    Print out a conclusive message to wrap up the game.
    '''
    print("Congratulations!!")
    
def process_guess(guess, goal):
    '''
    Print out whether or not the user was above, below,
    or at the goal.
    
    Args:
        guess (int): The number that the user entered
            as their guess.
        goal (int): The number that the computer is
            thinking of.
    '''
    # Branch execution based on whether the guess was right
    if guess < goal:
        print("You need to go higher!")
    elif guess > goal:
        print("You need to go lower!")
    else:
        print("That's correct, it's", goal)

def get_number():
    '''
    Ask the user for a number, and keep prompting
    them until they give you an actual number
    (as opposed to giving you a letter).
    '''
    # Get the guess from the user, returns a string
    number = input("guess the number between 1 and 10")
    # Was the string composed only of numbers?
    if number.isdigit():
        # If so, we can safely convert it to an integer
        number_as_int = int(number)
        # And return the result
        return number_as_int
    else:
        # Otherwise, call this function again recursively
        return get_number()

def main_game():
    '''
    Play a round of the game.
    '''
    # Pick random number between MINIMUM and MAXIMUM
    goal = randint(Lowest, Highest)
    # Initially, the user hasn't guessed anything.
    user_guess = None

    print_welcome()
    # Repeatedly ask the user until they get it right
    while user_guess != goal:
        user_guess = get_number()
        process_guess(user_guess, goal)
    print_ending()

# This if statement is common in most professional Python
#   programs - don't worry too much about what it does,
#   but you can safely assume it will work when you press
#   the run button.
if __name__ == '__main__':
    main_game()