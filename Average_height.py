# 🚨 Don't change the code below 👇
# 78, 65, 89, 86, 55, 91, 64, 89
# 77
student_heights = input("Input a list of student heights ").split(", ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


def find_average_height(heights):
    # Brush up on loops
    total_students = 0
    total_heights = 0
    for height in heights:
        total_students += 1
        total_heights += height
    return round(total_heights/total_students)


def find_average_height2(heights):
    # Brush up on loops
    return round(sum(heights)/len(heights))


print(find_average_height(student_heights))
print(find_average_height2(student_heights))
