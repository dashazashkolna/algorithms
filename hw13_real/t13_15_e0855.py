def generate_brackets(n):
    result = []

    def backtrack(current, stack, open_round, open_square):
        if len(current) == n:
            if not stack:
                result.append(current)
            return

        if open_round > 0:
            backtrack(current + '(', stack + ['('], open_round - 1, open_square)
        if open_square > 0:
            backtrack(current + '[', stack + ['['], open_round, open_square - 1)

        if stack:
            last = stack[-1]
            if last == '(':
                backtrack(current + ')', stack[:-1], open_round, open_square)
            elif last == '[':
                backtrack(current + ']', stack[:-1], open_round, open_square)

    backtrack("", [], n // 2, n // 2)
    return result


n = int(input())
for x in generate_brackets(n):
    print(x)