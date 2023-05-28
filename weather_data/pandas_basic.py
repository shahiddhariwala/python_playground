import pandas

data = pandas.read_csv("weather_data.csv")

# Converts to dictionary
data_dict = data.to_dict()
print(data_dict)

# Converts to list from series
temperatures = data["Temperature"].tolist()
print(temperatures)
print(f"Average temperature is {sum(temperatures) / len(temperatures)}'C")
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
