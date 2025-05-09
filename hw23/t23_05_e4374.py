def dfs(v, visited, graph):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited, graph)

def is_connected(n, edges, removed_edges):
    graph = [[] for _ in range(n + 1)]
    active_nodes = set()

    for i, (u, v) in enumerate(edges):
        if i not in removed_edges:
            graph[u].append(v)
            graph[v].append(u)
            active_nodes.add(u)
            active_nodes.add(v)

    if not active_nodes:
        return n <= 1

    visited = [False] * (n + 1)
    start_node = next(iter(active_nodes))
    dfs(start_node, visited, graph)

    for node in active_nodes:
        if not visited[node]:
            return False
    return True


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())

for _ in range(k):
    query = list(map(int, input().split()))
    removed = set(x - 1 for x in query[1:])
    result = is_connected(n, edges, removed)
    print("Connected" if result else "Disconnected")
