import random
from hangman_art import hangman_intro, hangman_step_art
import hangman_word

print(hangman_intro)

random_word = random.choice(hangman_word.random_words)


placeholder_string = ""
for _ in range(len(random_word)):
    placeholder_string += "_"


def check_if_letter_exist(letter):
    return letter in random_word


def update_letter_at_index(letter, index):
    global placeholder_string
    letter_list = list(placeholder_string)
    letter_list[index] = letter
    placeholder_string = "".join(letter_list)


def generate_placeholder_string(letter):
    for index in range(len(random_word)):
        if random_word[index] == letter:
            update_letter_at_index(letter, index)
    # return placeholder_string


error_count = 0
MAX_ALLOWED_ERROR = 6

while error_count <= MAX_ALLOWED_ERROR and placeholder_string != random_word:
    guess_letter = input("Guess a letter: ").lower()
    if check_if_letter_exist(guess_letter):
        generate_placeholder_string(guess_letter)
        print(f"You guessed it right, {placeholder_string}")
    else:
        error_count += 1
        print(f"{placeholder_string}")
        print(hangman_step_art[str(error_count)])

if placeholder_string == random_word:
    print(f"\n\nWord is: {random_word} => You win")
else:
    print(f"\n\nWord is: {random_word} => You lose")
