def prime_numbers():
    n = int(input("Enter any number :"))
    if n > 1 and n == 2:
        print(n, "is prime number")
        yield n
    if n % n == 0 and n % 2 != 0:
        print(n, " is a prime number")
        yield n
    elif n > 2 and n % 2 == 0:
        print(n, "It is not a prime number")
        yield n
prime_numbers()
next(prime_numbers())

