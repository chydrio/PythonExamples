def fibo(n):
    a, b = 0, 1
    while n:
        a, b, n = b, a + b, n - 1
    return a

print(fibo(100))
