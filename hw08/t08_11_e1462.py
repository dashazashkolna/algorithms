n = int(input())
s = []
while len(s) != n:
    a = list(map(int, input().split()))
    for x in a:
        s.append(x)

for i in range(1, n):
    key = s[i]
    j = i - 1
    while j >= 0 and (
        (s[j] % 10 > key % 10) or
        (s[j] % 10 == key % 10 and s[j] > key)
    ):
        s[j + 1] = s[j]
        j -= 1
    s[j + 1] = key

print(*s)
