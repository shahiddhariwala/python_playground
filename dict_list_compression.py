# List Compression
nums = [1, 2, 3, 4, 5, 6]
sqr_num = [num ** 2 for num in nums]
print(sqr_num)

even_nums = [num for num in range(1, 25) if num % 2 == 0]
print(even_nums)

# -----------
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def convert_to_f(temp_c):
    return round((temp_c * (9 / 5)) + 32, 1)


# Dict Compression
weather_f = {day: convert_to_f(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)
