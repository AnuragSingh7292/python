def factorial(n):
    if n==0:
        return 1
    else:
        return (n * factorial(n-1))
print(factorial(1))


def sum(n):
    if n==0:
        return 0
    else:
        return (n + sum(n-1))
print(sum(10))
