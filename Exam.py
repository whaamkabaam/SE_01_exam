'''
Reminder:

The repository must include:

- Your working code
- A README file including a short description, relevant notes, and most importantly instructions on
how to execute the program code (this may be, for example, a Python file, web page, or executable binary)
- A git commit history with more than a single commit documenting your work progress
'''
from turtle import Terminator

# ----------------------------------------------------------------------------------------------------------------------
# Task 1)
'''The first task is to implement the game without any hints.
Playing the game will be very difficult. But that’s ok for now. We just want to get the 
simplest possible version of the game to work:

X Display a welcome message to the user that explains the game.
X Allow the user to enter words.
X Display an error message to the user asking them to enter only exactly 5 characters if they didn’t.
- The player should have a total of 6 attempts to guess the word. 
  Every time they enter a word display to the user how many attempts they have left. 
  (If they didn’t type in 5 characters it should NOT count towards their attempts.)
- Define a 5-letter word the player has to guess in the code. //TODO Random Word library??
- End the game early if the player guessed the game and display a message to them that they have won.
- If after 6 attempts, the player hasn’t guessed the correct word, display a message telling them they have lost, 
  including what would have been the correct word.'''

def welcome():

    print('''Hi! Welcome to Wordle, your python nightmare of a game.
            To play, please just type your guess for the five letter word.''')
    '''player_ready = input("You ready? (y/n) ").lower()
    if player_ready == "y":
        print("Let's go!")
    elif player_ready == "n":
        print("hE wAsN't ReAdY.\nProgram terminated.")
        TODO how to termiante?'''

def user_input():

    is_guessing = True
    guess_counter = 0

    while is_guessing:
        try:
            user_word_guess = input(str("What word is your guess? "))
            if len(user_word_guess) != 5:
                print("This word isn't 5 characters long, please try again.")
            else:
                print("Nice guess...")
                guess_counter = + 1
                print(guess_counter)
                # is_guessing = False
        except Exception as E:
            print(E)
            print("That's not really a word, please try again.")

user_input()