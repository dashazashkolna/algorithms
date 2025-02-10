from math import *

def f(x):
    return x**2 + sqrt(x)

def solve(c):
    l = 0
    r = sqrt(c)
    while r - l > 1e-7:
        m = (l + r) / 2.0
        if f(m) < c:
            l = m
        else:
            r = m

    return (l + r) / 2.0

c = float(input())
print(f"{solve(c):.6f}")
