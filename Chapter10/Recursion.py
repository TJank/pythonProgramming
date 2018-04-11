# Factorial : n! = n*(n-1)!

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n-1)
    else:
        raise Exception("Number must be non-negative.")

fac = factorial(10)
print(fac)

# Fibonacci Sequence : 1 1 2 3 5 8 13 21 34 55 ...

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(8)
print(fib)


# Greatest Common Divisor
def gcd(x, y):
    x1 = abs(min(x, y))
    y1 = abs(max(x, y))
    gcd_ = x1

    if y1 % x1:
        gcd_ = gcd(x1, y1 % x1)
    return gcd_

g = gcd(92, 38)
print(g)

g = gcd(-252, 168)
print(g)

