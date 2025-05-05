def build_graph(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    return graph


def count_routes(graph, current, fin, d, visited):
    if d < 0:
        return 0
    if current == fin:
        return 1
    count = 0
    visited.add(current)
    if current in graph:
        for neighbor in graph[current]:
            if neighbor not in visited:
                count += count_routes(graph, neighbor, fin, d - 1, visited)
    visited.remove(current)
    return count


n, k, a, b, d = map(int, input().split())
edges = []
for x in range(k):
    u, v = map(int, input().split())
    edges.append((u,v))

graph = build_graph(edges)
res = count_routes(graph, a, b, d, set())

print(res)
