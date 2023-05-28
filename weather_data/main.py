import csv

with open("weather_data.csv", "r") as file:
    data = list(csv.reader(file))
    temperatures = []
    for row in data[1:]:
        temperatures.append(int(row[1]))
        print(row)

print(temperatures)
