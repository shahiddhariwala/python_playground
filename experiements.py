import requests
import datetime
import os

now = datetime.datetime.now()
for count in range(1, 1000):
    os.system("cls")
    print("Current progress: ", count)
    requests.get("https://komarev.com/ghpvc/?username=shahiddhariwala&style=plastic")
then = datetime.datetime.now()

print(f"Success ! count increased by 1000\n it took {(then - now).total_seconds()} seconds")
