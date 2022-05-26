def fibo(n):
    print("Al", n, "-lea numar din sirul lui Fibonacci este:")
    x = 0
    y = 1
    s = None
    no = 2
    if n == 1:
        print(x)
    elif n == 2:
        print(y)
    while no < n:
        s = x + y
        x = y
        y = s
        no += no
    return s


print(fibo(2))
