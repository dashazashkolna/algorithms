from math import *

def f(x):
    return sin(x) - x/3

def solve():
    l = 1.6
    r = 3
    while f(r) - f(l) > 1e-7:
        m = (l + r) / 2.0
        if f(m) > 0:
            r = m
        else:
            l = m

    return (l + r) / 2.0

print(f"{solve():.6f}")     #2.300000
