# Different approaches for generating Fibonacci numbers
#
# First attempt just shows what happens if you forget a base case
#


# Naive attempt with base case
def fib2(n):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


# Use memoization
MEMO = {0: 0, 1: 1}

def fib3(n):
    if n not in MEMO:
        MEMO[n] = fib3(n-1) + fib3(n-2)
    return MEMO[n]


# Use automatic memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n):
    if n < 2:
        return n
    return fib4(n-2) + fib4(n-1)


# A simple iterative approach is the most performant
def fib5(n):
    if n == 0: return n
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


# Use a generator to generate a sequence up to a given value
def fib6(n):
    yield 0
    if n > 0: yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next



if __name__ == '__main__':
    assert fib2(0) == 0
    assert fib2(1) == 1
    assert fib2(9) == 34

    assert fib3(0) == 0
    assert fib3(1) == 1
    assert fib3(9) == 34
    assert fib3(50) == 12586269025

    assert fib4(0) == 0
    assert fib4(1) == 1
    assert fib4(9) == 34
    assert fib4(50) == 12586269025

    assert fib5(0) == 0
    assert fib5(1) == 1
    assert fib5(9) == 34
    assert fib5(50) == 12586269025

    # Use the generator
    for i in fib6(50):
        print(i)