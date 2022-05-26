def prime(n):
    print("The prime numbers smaller than", n, "are:")

    np = 2

    for np in range(2, n):
        for i in range(2, np):
            if np % i == 0:
                break
        else:
            print(np)

prime(102)



