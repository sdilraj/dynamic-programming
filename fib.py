def fib(num):
    if num == 1 | num == 2:
        result = 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result