def permutations(n, k):
    used = [False] * (n + 1)
    current = []
    result = []

    def backtrack():
        if len(current) == k:
            result.append(current.copy())
            return
        for num in range(1, n + 1):
            if not used[num]:
                used[num] = True
                current.append(num)
                backtrack()
                current.pop()
                used[num] = False

    backtrack()
    return result


n, k = map(int, input().split())
permutations = permutations(n, k)
for perm in permutations:
    print(' '.join(map(str, perm)))
