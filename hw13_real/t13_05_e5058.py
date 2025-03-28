def is_valid(s):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[char]:
                return "no"

    return "yes" if not stack else "no"


if __name__ == '__main__':
    print(is_valid(input()))