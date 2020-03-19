def fib(num, mem): # using memoziation
    if mem[num] != num:
        return mem[num]
    else:
        result = fib (num - 1) + fib (num - 2)
        mem[num] = result
        return result