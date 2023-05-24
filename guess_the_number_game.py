import os
import random
art = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""


MAX_NUMBER_OF_EASY_ATTEMPTS = 10
MAX_NUMBER_OF_HARD_ATTEMPTS = 5
number_of_attempts = MAX_NUMBER_OF_HARD_ATTEMPTS
user_guess_value = 0


def get_difficulty_level():
    return input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()


def start_game():
    global number_of_attempts, user_guess_value
    os.system("clear")
    print(art)
    print(
        f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {random.randint(1,100)}")
    target_value = random.randint(1, 100)

    if get_difficulty_level() == "easy":
        number_of_attempts = MAX_NUMBER_OF_EASY_ATTEMPTS

    def check_if_game_over():
        """
        Checks if game is over or to continue the game
        Declare winner if correct choice is given by user
        """
        is_game_over = True
        if user_guess_value == target_value:
            print("You guessed it right! 😎")
        elif number_of_attempts == 0:
            print(
                f"You've run out of guesses, you lose.")
        else:
            is_game_over = False
        return is_game_over

    def start_guessing():
        '''
        Actual logic is written here to get user input
        '''
        global number_of_attempts, user_guess_value
        print(
            f"You have {number_of_attempts} attempts remaining to guess the number.")
        number_of_attempts -= 1
        user_guess_value = int(input("Make a guess: "))
        if not check_if_game_over():
            if user_guess_value > target_value:
                print("Too High.\nGuess again")
            else:
                print("Too Low.\nGuess again")
            start_guessing()
    start_guessing()


while input("Do you want to play number guessing game? Type 'y' or 'n': ").lower() == "y":
    start_game()
