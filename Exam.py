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

- After every attempt (and only if the user typed in a 5-letter word),
  compare each letter the player typed in with the letters from the correct solution.
  Then, display a hint to the player telling them which of the letters are in the word.
  That’s the first hint.
- Ensure that it doesn’t matter whether the user typed in lowercase or uppercase letters.
- For the second hint, compare the position of the letters the player entered with the position
  of the letters in the correct word.
  Display to the user the numbers of the positions that contain the correct letters.
- Ensure to account for the situation that in either of the two hints there could be no matching letters
  or no correct positions. In that case, tell that to the user, e.g., by displaying the word “none.” (see example)'''

def welcome():

    print('''Hi! Welcome to Wordle, your python nightmare of a game.
    To play, please just type your guess for the five letter word.''')
    '''player_ready = input("You ready? (y/n) ").lower()
    if player_ready == "y":
        print("Let's go!")
    elif player_ready == "n":
        print("hE wAsN't ReAdY.\nProgram terminated.")
        TODO how to termiante? // UPDATE: imported something random but didnt work'''

def guessing_main():

    is_guessing = True
    guess_counter = 0
    guesses_left = 6

    while is_guessing:

        try:
            user_word_guess = (input(str("What word is your guess? "))).lower()
            if len(user_word_guess) != 5:
                print("This word isn't 5 characters long, please try again.")
            elif user_word_guess == final_word:
                is_guessing = False
                guess_counter += 1
                success(guess_counter)
            elif len(user_word_guess) == 5:
                print("Nice guess...")
                guess_counter += 1
                guesses_left -= 1
                print(f"You have {guesses_left} guesses left.")
                word_compare(final_word, user_word_guess)
                if guesses_left < 1:
                    is_guessing = False
                    player_sucks()
            else:
                print("You reached unknown land. How did you get here?")

        except Exception as E:
            print(E)
            print("That's not really a word or the dev f*cked up, please try again.")

def success(guess_counter):

    print("OMG! You guessed first try. So legendary.") if guess_counter < 2 else print(f"Success! You guessed {final_word} in {guess_counter} attempts.")

def player_sucks():

    print("whomp whomp, you lost.")
    print(f"The correct word would have been {final_word}.")

def word_compare(final_world, user_word_guess):

    split_final_word = list(final_world)
    split_guessed_word = list(dict.fromkeys(user_word_guess)) # this is to remove duplicate letters
    # if we dont do this the print of the letter being in the word loops that amount of times
    letter_matches = [] # list of all matching letters

    for letter in split_guessed_word:

        if letter in split_final_word:
            letter_matches += letter

    if letter_matches:

        print(letter_matches)
        print(", ".join(letter_matches)) # TESTING makes it pretty
        print(f"The letter(s) {letter_matches} of your guessed word '{user_word_guess}' is in the word you are guessing.")



final_word = "apple"
welcome()
guessing_main()