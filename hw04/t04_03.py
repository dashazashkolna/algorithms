def f(x):
    return x**3 + x - 4

def solve():
    l = 0
    r = 10
    while r - l > 1e-7:
        m = (l + r) / 2.0
        if f(m) > 0:
            r = m
        else:
            l = m

    return (l + r) / 2.0

print(f"{solve():.6f}")     #1.378797
