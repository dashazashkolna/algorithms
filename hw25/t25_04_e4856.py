from collections import deque


def bellman_ford(n, edges, start, end):
    INF = float('inf')
    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)
    dist[start] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                prev[u] = v
                updated = True
        if not updated:
            break

    if dist[end] == INF:
        return -1, []

    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    return dist[end], path


n, m = map(int, input().split())
s, f = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    edges.append((v, u, w))
distance, path = bellman_ford(n, edges, s, f)

if distance == -1:
    print(-1)
else:
    print(distance)
    print(' '.join(map(str, path)))
