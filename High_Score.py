# 🚨 Don't change the code below 👇
# 78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

heightest_score = student_scores[0]

for student_score in student_scores:
    if heightest_score < student_score:
        heightest_score = student_score

print(f"The highest score in the class is: {heightest_score}")
print(f"The highest score in the class is: {max(student_scores)}")
