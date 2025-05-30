import sys
sys.set_int_max_str_digits(10**6)


def multiply_recursive(u, v):
    if u < 10 or v < 10:
        return u * v

    digits = max(len(str(u)), len(str(v)))
    split = digits // 2

    a, b = divmod(u, 10 ** split)
    c, d = divmod(v, 10 ** split)

    ac = multiply_recursive(a, c)
    bd = multiply_recursive(b, d)
    abcd = multiply_recursive(a + b, c + d)

    mid = abcd - ac - bd

    return (ac * 10 ** (2 * split)) + (mid * 10 ** split) + bd

if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    output = multiply_recursive(num1, num2)
    print(output)
