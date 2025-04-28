n, m = map(int, input().split())
edges = set()

for _ in range(m):
    u, v = map(int, input().split())
    edges.add((u, v))

if len(edges) == m:
    print("NO")
else: print("YES")

