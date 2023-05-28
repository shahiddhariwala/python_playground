import pandas

data = pandas.read_csv("weather_data.csv")

# Converts to dictionary
data_dict = data.to_dict()
print(data_dict)

# Converts to list from series
temperatures_series = data["Temperature"]
temp_list = temperatures_series.tolist()

print(temp_list)
print(f"Average temperature is {sum(temp_list) / len(temp_list)}'C")

# Pandas inbuilt methods

# Get mean or average
print(f"Average temperature is {temperatures_series.mean()}'C")

# Get max temperature
max_temp = temperatures_series.max()
print(data[data.Temperature == max_temp])

# Create dataframe from scratch

import random

# List of class names
classes = ["1st std", "2nd std", "3rd std", "4th std", "5th std", "6th std", "7th std", "8th std", "9th std",
           "10th std", "11th std", "12th std"]

# Dictionary with class and number of students
class_students = {
    "class": classes,
    "students": [random.randint(10, 30) for _ in classes]  # List compression: Generating random number of students for
    # each class this is called list compression
}

class_data = pandas.DataFrame(class_students)
print(class_data)
"""

print(data)
print(data["Temperature"])
Beautifully printed by pandas
         Day  Temperature      Condition
0     Monday           25          Sunny
1    Tuesday           22         Cloudy
2  Wednesday           27          Rainy
3   Thursday           24  Partly Cloudy
4     Friday           26          Sunny
5   Saturday           23          Rainy
6     Sunday           21         Cloudy


0    25
1    22
2    27
3    24
4    26
5    23
6    21
Name: Temperature, dtype: int64
"""
