n, m = map(int, input().split())
edges = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    edges[u] += 1
    edges[v] += 1

for v in range(1, n + 1):
    print(edges[v])