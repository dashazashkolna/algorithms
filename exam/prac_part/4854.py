n = int(input())
res = [[] for _ in range(n)]

for i in range(n):
    line = input().strip()
    if line:
        edges = list(map(int, line.split()))
        for v in edges:
            res[v - 1].append(i + 1)

print(n)
for i in range(n):
    res[i].sort()
    print(' '.join(map(str, res[i])))
