import random


def printHeads():
    print("Heads")


def printTails():
    print("Tails")


random_num = random.randint(0, 1)

if (random_num == 0):
    printTails()
else:
    printHeads()
