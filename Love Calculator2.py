# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

true_letters = list("true")
love_letters = list("love")
combined_names = str.lower(name1 + name2)
true_count = 0
love_count = 0
for letter in true_letters:
    true_count += combined_names.count(letter)

for letter in love_letters:
    love_count += combined_names.count(letter)


score = int(str(true_count)+str(love_count))
if score < 10 or score > 80:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")

# Jack Bauer
# Angela Yu
# Should come 53
