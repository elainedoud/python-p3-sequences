def print_fibonacci(length):
    thisList = []
    x = 0
    y = 1
    if (length == 0):
        print(thisList)
    else:
        for i in range(length):
            thisList.append(x)
            x, y = y, x + y
        print(thisList)
