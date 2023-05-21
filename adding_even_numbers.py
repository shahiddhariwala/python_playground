def manual_way():
    sum = 0
    counter = 2

    while counter <= 100:
        sum += counter
        counter += 2
    print(sum)


def manual_way_2():
    sum = 0
    counter = 2

    for counter in range(2, 101, 2):
        sum += counter
    print(sum)


def smart_way():
    print(sum(range(2, 101, 2)))


manual_way()
manual_way_2()
smart_way()
