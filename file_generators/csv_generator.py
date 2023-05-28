import csv

data = [
    ["Day", "Temperature", "Condition"],
    ["Monday", 25, "Sunny"],
    ["Tuesday", 22, "Cloudy"],
    ["Wednesday", 27, "Rainy"],
    ["Thursday", 24, "Partly Cloudy"],
    ["Friday", 26, "Sunny"],
    ["Saturday", 23, "Rainy"],
    ["Sunday", 21, "Cloudy"]
]

filename = "../weather_data/weather_data.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"The {filename} file has been created.")
