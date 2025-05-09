import sys
input = sys.stdin.read

def dfs(start, graph, visited, component):
    stack = [start]
    visited[start] = True
    while stack:
        v = stack.pop()
        component.append(v + 1)
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                stack.append(u)

data = input().split()
n = int(data[0])
m = int(data[1])

graph = [[] for _ in range(n)]
index = 2
for _ in range(m):
    u = int(data[index]) - 1
    v = int(data[index + 1]) - 1
    graph[u].append(v)
    graph[v].append(u)
    index += 2

visited = [False] * n
components = []

for v in range(n):
    if not visited[v]:
        component = []
        dfs(v, graph, visited, component)
        components.append(component)

output = [str(len(components))]
for comp in components:
    output.append(str(len(comp)))
    output.append(' '.join(map(str, comp)))

print('\n'.join(output))
