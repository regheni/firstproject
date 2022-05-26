def fibo(n):
    print("The", n, "th number of the Fibonacci sring is:")
    x = 0
    y = 1
    s = None
    no = 2
    if n == 1:
        print(x)
    elif n == 2:
        print(y)
    while no < n:
        s = y + x
        x = y
        y = s
        no += 1
    return s


print(fibo(8))
