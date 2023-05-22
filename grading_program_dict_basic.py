student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for key in student_scores:
    score = student_scores[key]
    grade = ""
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81 and score <= 90:
        grade = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade


# 🚨 Don't change the code below 👇
print(student_grades)
