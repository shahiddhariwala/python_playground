import os
import random
art = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

number_of_attempts = 5
user_guess_value = 0


def start_game():
    global number_of_attempts, user_guess_value
    os.system("clear")
    print(
        f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nPssst, the correct answer is {random.randint(1,100)}")
    difficulty_level = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()
    target_value = random.randint(1, 100)

    user_guess_value = 0
    if difficulty_level == "easy":
        number_of_attempts = 10
        # You have 5 attempts remaining to guess the number.
        # Make a guess: 33

    def check_winner():
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
        global number_of_attempts, user_guess_value
        print(
            f"You have {number_of_attempts} attempts remaining to guess the number.")
        number_of_attempts -= 1
        user_guess_value = int(input("Make a guess: "))
        if not check_winner():
            if user_guess_value > target_value:
                print("Too High.\nGuess again")
            else:
                print("Too Low.\nGuess again")
            start_guessing()
    start_guessing()


while input("Do you want to play number guessing game? Type 'y' or 'n': ").lower() == "y":
    start_game()
