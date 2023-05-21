# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def get_person(names):
    total_person = len(names)
    index = random.randint(0, total_person-1)
    return names[index]


def get_person_via_choice(names):
    return random.choice(names)


print(f"{get_person(names)} is going to buy the meal today!")
print(f"{get_person_via_choice(names)} is going to buy the meal today!")
