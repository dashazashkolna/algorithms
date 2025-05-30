def solve(index, left, right, weights, total, possible):
    if index == total:
        if left == right:
            possible.add(left)
        return
    w = weights[index]
    solve(index + 1, left, right, weights, total, possible)
    solve(index + 1, left + w, right, weights, total, possible)
    solve(index + 1, left, right + w, weights, total, possible)


count, weight_count = map(int, input().split())
weights = list(map(int, input().split()))
disk_weights = list(map(int, input().split()))

balanced = set()
solve(0, 0, 0, disk_weights, weight_count, balanced)

final = {bar + 2 * bal for bar in weights for bal in balanced}
for val in sorted(final):
    print(val)
