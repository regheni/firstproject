def dividers(x):
    print("The dividers of number", x, "are:")
    y = 1
    while y <= x:
        if x % y == 0:
            print(y)
        y += 1


dividers(10)
