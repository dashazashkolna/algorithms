n = int(input())
s = []
for x in range(n):
    a, b, c = map(int, input().split())
    z = a * 10000 + b * 100 + c
    s.append((z, a, b, c))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if s[j][0] < s[min_index][0]:
            min_index = j
    s[i], s[min_index] = s[min_index], s[i]

for x in s:
    print(x[1], x[2], x[3])