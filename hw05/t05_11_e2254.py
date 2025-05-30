R, L, B = map(int, input().split())

x = []
for _ in range(R):
    x.append(int(input()))


prefix = [0] * (R + 1)
for i in range(R):
    prefix[i+1] = prefix[i] + x[i]

left = 0
right = R
best = 0

while left <= right:
    mid = (left + right) // 2
    found = False

    for i in range(R - mid + 1):
        j = i + mid
        median_pos = (i + j) // 2

        left_sum = x[median_pos] * (median_pos - i) - (prefix[median_pos] - prefix[i])
        right_sum = (prefix[j] - prefix[median_pos]) - x[median_pos] * (j - median_pos)
        total_cost = left_sum + right_sum

        if total_cost <= B:
            found = True
            break

    if found:
        best = mid
        left = mid + 1
    else:
        right = mid - 1

print(best)
