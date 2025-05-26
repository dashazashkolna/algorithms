import heapq


def prim(n, graph):
    used = [False] * (n + 1)
    mst_edges = set()
    min_heap = [(0, 1, -1)]
    total_edges = 0

    while min_heap and total_edges < n - 1:
        w, u, parent = heapq.heappop(min_heap)
        if used[u]:
            continue
        used[u] = True
        if parent != -1:
            mst_edges.add((min(u, parent), max(u, parent)))
            total_edges += 1
        for v, weight in graph[u]:
            if not used[v]:
                heapq.heappush(min_heap, (weight, v, u))
    return mst_edges


t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    edge_map = {}

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edge_map[(min(u, v), max(u, v))] = w

    mst = prim(n, graph)
    if (min(p, q), max(p, q)) in mst:
        print("YES")
    else:
        print("NO")
