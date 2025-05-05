# Instructions
'''
Reminder:

The repository must include:

- Your working code
- A README file including a short description, relevant notes, and most importantly instructions on
how to execute the program code (this may be, for example, a Python file, web page, or executable binary)
- A git commit history with more than a single commit documenting your work progress
'''

# ----------------------------------------------------------------------------------------------------------------------
# Task 1)
'''The first task is to implement the game without any hints.
Playing the game will be very difficult. But that’s ok for now. We just want to get the 
simplest possible version of the game to work:

X Display a welcome message to the user that explains the game.
X Allow the user to enter words.
X Display an error message to the user asking them to enter only exactly 5 characters if they didn’t.
X The player should have a total of 6 attempts to guess the word. 
  Every time they enter a word display to the user how many attempts they have left. 
  (If they didn’t type in 5 characters it should NOT count towards their attempts.)
X Define a 5-letter word the player has to guess in the code.
X End the game early if the player guessed the game and display a message to them that they have won.
X If after 6 attempts, the player hasn’t guessed the correct word, display a message telling them they have lost, 
  including what would have been the correct word.'''

# ----------------------------------------------------------------------------------------------------------------------
# Task 2)
'''Now, it’s time to implement the two hints.
Complete one hint at a time and try not to work on too many things at once.

X After every attempt (and only if the user typed in a 5-letter word),
  compare each letter the player typed in with the letters from the correct solution.
  Then, display a hint to the player telling them which of the letters are in the word.
  That’s the first hint.
X Ensure that it doesn’t matter whether the user typed in lowercase or uppercase letters.
X For the second hint, compare the position of the letters the player entered with the position
  of the letters in the correct word.
  Display to the user the numbers of the positions that contain the correct letters.
X Ensure to account for the situation that in either of the two hints there could be no matching letters
  or no correct positions. In that case, tell that to the user, e.g., by displaying the word “none.” (see example)
  --> Prof said current logic is fine, it only shows info when there is a positive guess'''

# ----------------------------------------------------------------------------------------------------------------------
# Task 3)
'''Your last task is to polish the game and allow for it to be played multiple times.

- After the player has either lost or won, ask the player if they wish to play again. Exit the game if they don’t.
- If the player does want to play again, start a new round with a new word.
  Ensure that the next round is played with a different word than before.
- Allow the player to play at least 3 games with different words.
- Allow the player to exit the game any time - e.g., by entering the word ‘exit’.'''

import os

def welcome():

    print('''Hi! Welcome to Wordle, your python nightmare of a game.
    To play, please just type your guess for the five letter word.''')
    '''player_ready = input("You ready? (y/n) ").lower()
    if player_ready == "y":
        print("Let's go!")
    elif player_ready == "n":
        print("hE wAsN't ReAdY.\nProgram terminated.")
        TODO how to termiante? // UPDATE: imported something random but didnt work'''

def game_manager(round_counter): # manages if the player wants to play another round

    player_is_choosing = True # boolean to enter infinite loop until player has chosen
    round_counter += 1
    word_final = ""

    # declaring which word will be used to play with / to be guessed

    while player_is_choosing:

        if round_counter == 1:
            word_final = "apple"
            guessing_main(word_final)

        if round_counter == 2:
            word_final = "chair"

        elif round_counter == 3:
            word_final = "table"

        elif round_counter > 3:  # if its more than three rounds it quits
            print("Unfortunately you have reached the daily limit of games. Come back tomorrow!")
            exit()

        print("Thank you for playing.")
        continue_input = input("Do you wish to continue playing? (y/n) ")
        if continue_input.lower() == "y":
            player_is_choosing = False
            guessing_main(word_final)

        elif continue_input.lower() == "n":
            player_is_choosing = False
            print("Still, thank you for playing.")

        else:
            print("Invalid input, DWDAWDplease try again.")

    return round_counter

def success(guess_counter, to_be_guessed_word): # success function

    print("OMG! You guessed first try. So legendary.") if guess_counter < 2 else print(f"Success! You guessed {to_be_guessed_word} in {guess_counter} attempts.")
    game_manager()

def player_sucks(to_be_guessed_word): # loss function

    print("whomp whomp, you lost.")
    print(f"The correct word would have been {to_be_guessed_word}.")

def guessing_main(word_final):

    to_be_guessed_word = word_final
    is_guessing = True # condition to enter infinite loop until player wins or runs out of guesses
    guess_counter = 0
    guesses_left = 6

    while is_guessing:
        try:
            user_word_guess = (input(str("What word is your guess? "))).lower() # makes sure to disregard caps
            if len(user_word_guess) != 5: # invalid input checker
                print("This word isn't 5 characters long, please try again.")
            elif user_word_guess == to_be_guessed_word: # correct guess
                is_guessing = False
                guess_counter += 1
                success(guess_counter, to_be_guessed_word) # calls success function
            elif len(user_word_guess) == 5: # correct input but invalid guess
                print("Nice guess...")
                guess_counter += 1
                guesses_left -= 1
                print(f"You have {guesses_left} guesses left.")
                word_compare(to_be_guessed_word, user_word_guess) # calls comparing function
                if guesses_left < 1: # is called when player has put correct input but has run out of guesses
                    is_guessing = False
                    player_sucks(to_be_guessed_word) # legendarily named loosing function is called
            else:
                print("You reached unknown land. How did you get here?") # honestly no clue how anyone would end up here

        except Exception as E: # if anything goes wrong i can troubleshoot without the program crashing
            print(E)
            print("The dev f*cked up, please try again.")

def word_compare(to_be_guessed_word, user_word_guess): # word comparing function

    split_final_word = list(to_be_guessed_word)
    split_guessed_word_raw = list(user_word_guess)
    split_guessed_word = list(dict.fromkeys(user_word_guess)) # this is to remove duplicate letters
    # if we dont do this the print of the letter being in the word loops that amount of times
    letter_matches = [] # list of all matching letters
    letter_position_matches = [] # list of matching letters that also match position

    for letter in split_guessed_word: # iterate and build the list of matching letters

        if letter in split_final_word:
            letter_matches += letter

    if letter_matches: # if there are any matching letters this gets executed and informs the player

        print(f"The letter {", ".join(letter_matches)} of your guessed word '{user_word_guess}' is in the word you are guessing.") \
        if len(letter_matches) < 2 else print(f"The letters {", ".join(letter_matches)} of your guessed word '{user_word_guess}' are in the word you are guessing.")
        # i felt fancy doing this, lmk if this is ugly code - just to have better syntax when printing success message

    for index, matched_letters in enumerate(split_final_word):
        # this compares positions of matching letters of the guessed word and the word to be guessed

        if split_guessed_word_raw[index] == split_final_word[index]:
            letter_position_matches += matched_letters

    if letter_position_matches: # if there are any matching letters + positions this gets executed and informs the player
        print(f"So you're getting there! And even better: {", ".join(letter_position_matches)} is a position match.") \
            if len(letter_position_matches) < 2 else print(f"Even better: {", ".join(letter_position_matches)} are a position match.")
        # same thing here with better syntax


welcome()
round_counter = 0
game_manager(round_counter)