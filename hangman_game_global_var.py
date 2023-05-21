import random

hangman_intro = '''
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"     
'''

hangman_step_art = {
    "1": '''
          _______
     |/      |
     |      (_)
     |       
     |       
     |      
     |
 ____|___
    ''',
    "2": '''
          _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___
    ''',
    "3": '''
          _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ____|___
    ''',
    "4": '''
          _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ____|___
    ''',
    "5": '''
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___
    ''',
    "6": '''
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___
    ''',
    "7": '''
          _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___
    ''',
}
print(hangman_intro)

random_words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'goat', 'house', 'key', 'lion', 'monkey',
                'orange', 'pen', 'queen', 'robot', 'snake', 'tree', 'umbrella', 'video', 'whale', 'xray', 'yoyo', 'zebra']


random_word = random.choice(random_words)


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
        print(f"Current string is {placeholder_string}")
    else:
        error_count += 1
        print(f"Current string is {placeholder_string}")
        print(hangman_step_art[str(error_count)])

if placeholder_string == random_word:
    print(f"Word is: {random_word}: You win")
else:
    print(f"Word is: {random_word}: You lose")
