# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

true_letters = list("true")
love_letters = list("love")
true_count = 0
love_count = 0
for letter in name1:
    if str.lower(letter) in true_letters:
        true_count += 1
    if str.lower(letter) in love_letters:
        love_count += 1

for letter in name2:
    if str.lower(letter) in true_letters:
        true_count += 1
    if str.lower(letter) in love_letters:
        love_count += 1

score = int(str(true_count)+str(love_count))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

# Jack Bauer
# Angela Yu
# Should come 53
