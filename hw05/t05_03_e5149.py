def can_place(stalls, cows, min_length):
    k = 1
    cur_pos = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - cur_pos >= min_length:
            cur_pos = stalls[i]
            k += 1
            if k == cows:
                return True

    return False


def max_length(stalls, cows):
    stalls.sort()
    l, r = 1, stalls[-1] - stalls[0]
    res = 0

    while l <= r:
        m = (l + r) // 2
        if can_place(stalls, cows, m):
            res = m
            l = m + 1
        else:
            r = m - 1

    return res


n, k = map(int, input().split())
stalls = list(map(int, input().split()))

print(max_length(stalls, k))
