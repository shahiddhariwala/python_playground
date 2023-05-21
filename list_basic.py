import random
states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh",
    "Dadra and Nagar Haveli",
    "Daman and Diu",
    "Lakshadweep",
    "Puducherry"
]


print(states[0])
print(states[-1])
states.append("ShahidLand")
print(states[-1])
states.remove(states[-1])
print(states[-1])
states.extend(["Pokemon", "Bleach"])
print(states[-3:])
states.pop()
states.pop()
print(states[-3:])

"""
The `choice()` function in Python randomly selects an element from a sequence. The sequence can be a list, a tuple, a range, a string, or any other iterable object.

To use the `choice()` function, you first need to import the `random` module. Then, you can use the `choice()` function to select a random element from the sequence.

For example, the following code randomly selects a state from the list of states in India:


import random

states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "Puducherry"]

random_state = random.choice(states)

print(random_state)


This code will print a random state from the list. Each time you run the code, a different state will be printed.

The `choice()` function can also be used to select a random number from a range. For example, the following code randomly selects a number from 1 to 10:

```
import random

random_number = random.choice(range(1, 11))

print(random_number)
```

This code will print a random number from 1 to 10. Each time you run the code, a different number will be printed.
"""
random_state = random.choice(states)

print(random_state)
