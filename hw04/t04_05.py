from math import *

def f(x):
    return x**3 + 4*x**2 + x - 6

def solve():
    l = 0
    r = 2
    while f(r) - f(l) > 1e-7:
        m = (l + r) / 2.0
        if f(m) > 0:
            r = m
        else:
            l = m

    return (l + r) / 2.0

print(f"{solve():.6f}")
