n, m = map(int, input().split())
inp = [0] * (n + 1), out = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    out[u] += 1
    inp[v] += 1

for v in range(1, n + 1):
    print(inp[v], out[v])