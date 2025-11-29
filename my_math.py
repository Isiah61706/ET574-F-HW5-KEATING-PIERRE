#Author: [Isiah Keating-Pierre], QCC ID: [24603122]

# my_math.py

# def fibonacci(n):
#     """
#     Return the n-th Fibonacci number (0-indexed).
#     Raises:
#         TypeError: if n is not an int
#         ValueError: if n is negative
#     """
#     if not isinstance(n, int):
#         raise TypeError("fibonacci(n) requires an integer n")
#     if n < 0:
#         raise ValueError("n must be non-negative")

#     if n < 2:
#         return n

#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b


# def mean(values):
#     """
#     Return the arithmetic mean of a non-empty iterable of numbers.
#     Raises:
#         ValueError: if values is empty
#         TypeError: if any element is not a number
#     """
#     total = 0.0
#     count = 0

#     for v in values:
#         if not isinstance(v, (int, float)):
#             raise TypeError("mean() expects all elements to be numbers")
#         total += float(v)
#         count += 1

#     if count == 0:
#         raise ValueError("mean() of empty data")

#     return total / count


def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

def isEven(x):
    return x % 2 ==0

def area_of_circle(r):
    if r < 0:
        raise ValueError("Radius cannot be negative.")

    pi = 3.14159
    return pi * r * r

def sum_of_digits(n):
    n = abs(n)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total