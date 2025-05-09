from collections import deque

def topological_sort(n, edges):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) == n:
        print(*result)
    else:
        print(-1)

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

topological_sort(n, edges)
