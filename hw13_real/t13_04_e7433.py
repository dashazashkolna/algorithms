def convert(number: int, to_base: int) -> str:
    stack = []
    while number > 0:
        stack.append(number % to_base)
        number //= to_base

    res = ""
    while stack:
        res += get_res(stack.pop())
    return res


def get_res(n: int) -> str:
    if n < 10:
        return str(n)
    else:
        return f"[{n}]"


if __name__ == '__main__':
    n = int(input())
    base = int(input())
    print(convert(n, base))