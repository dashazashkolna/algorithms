from sys import setrecursionlimit
setrecursionlimit(10000)

def solve(n, edges):
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u - 1].append(v - 1)
        reverse_graph[v - 1].append(u - 1)

    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    scc_count = 0

    def dfs2(u):
        visited[u] = True
        for v in reverse_graph[u]:
            if not visited[v]:
                dfs2(v)

    for u in reversed(order):
        if not visited[u]:
            dfs2(u)
            scc_count += 1

    return scc_count


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, edges))
