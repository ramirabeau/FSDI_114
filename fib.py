def fib(n):
    if n < 2: # base case
        return n
    return fib(n-1) + fib(n-2)