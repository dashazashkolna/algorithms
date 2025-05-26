import heapq


def build_mst(n, adj, exclude=None, force_include=None):
    visited = [False] * (n + 1)
    heap = []
    mst_edges = []
    total_cost = 0

    if force_include:
        a, b, c = force_include
        visited[a] = visited[b] = True
        mst_edges.append((a, b, c))
        total_cost += c
        for node in (a, b):
            for neighbor, cost in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(heap, (cost, node, neighbor))
    else:
        visited[1] = True
        for neighbor, cost in adj[1]:
            if exclude and ((1, neighbor) == exclude or (neighbor, 1) == exclude):
                continue
            heapq.heappush(heap, (cost, 1, neighbor))

    while heap and len(mst_edges) < n - 1:
        cost, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        if exclude and ((u, v) == exclude or (v, u) == exclude):
            continue
        visited[v] = True
        mst_edges.append((u, v, cost))
        total_cost += cost
        for neighbor, new_cost in adj[v]:
            if not visited[neighbor]:
                heapq.heappush(heap, (new_cost, v, neighbor))

    if len(mst_edges) == n - 1:
        return total_cost, mst_edges
    return float('inf'), []

def two_min(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        adj[a].append((b, c))
        adj[b].append((a, c))

    s1, mst_edges = build_mst(n, adj)
    s2 = float('inf')

    for a, b, _ in mst_edges:
        cost, _ = build_mst(n, adj, exclude=(a, b))
        s2 = min(s2, cost)

    mst_set = {(min(a, b), max(a, b), c) for a, b, c in mst_edges}
    for a, b, c in edges:
        edge_id = (min(a, b), max(a, b), c)
        if edge_id not in mst_set:
            cost, _ = build_mst(n, adj, force_include=(a, b, c))
            s2 = min(s2, cost)

    return s1, s2


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

s1, s2 = two_min(n, edges)
print(s1, s2)