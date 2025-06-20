BRACKETS = {"(": ")", "[": "]", "{": "}"}

def check(string):
    stack = []

    for x in string:
        if x in BRACKETS:
            stack.append(x)
        elif len(stack) == 0 or BRACKETS[stack.pop()] != x:
            return False

    return len(stack) == 0


input_string = input().strip()
print("YES" if check(input_string) else "NO")