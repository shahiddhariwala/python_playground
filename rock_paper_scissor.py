import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

"""
Rock wins against scissor
Scissor wins against paper
Paper wins against Rock
"""


choices = ["rock", "paper", "scissors"]
choices_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}
user_choice = choices[int(
    input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")) % 3]


def generate_computer_choice():
    return choices[random.randint(0, 2)]


computer_choice = generate_computer_choice()


def check_who_won(user_c, computer_c):
    # Rules
    if (user_c == computer_c):
        winner = "draw"
    elif user_c == "rock":
        if computer_c == "scissors":
            winner = "user"
        else:
            winner = "computer"
    elif user_c == "paper":
        if computer_c == "rock":
            winner = "user"
        else:
            winner = "computer"
    elif user_c == "scissors":
        if computer_c == "paper":
            winner = "user"
        else:
            winner = "computer"
    return winner


print(choices_art[user_choice])

print(f"Computer Choose:\n{choices_art[computer_choice]}")

winner = check_who_won(user_choice, computer_choice)
if winner == "user":
    print("You won")
elif winner == "computer":
    print("You lost")
else:
    print("Its draw")
