from collections import deque

def get_neighbors(num):
    s = str(num)
    neighbors = []
    if s[0] != '9':
        neighbors.append(str(int(s[0]) + 1) + s[1:])

    if s[3] != '1':
        neighbors.append(s[:3] + str(int(s[3]) - 1))

    neighbors.append(s[-1] + s[:3])
    neighbors.append(s[1:] + s[0])

    return [n for n in neighbors if '0' not in n]

def bfs(start, end):
    queue = deque()
    visited = set()
    prev = {}

    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()
        if current == end:
            break

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                prev[neighbor] = current
                queue.append(neighbor)

    path = []
    current = end
    while current != start:
        path.append(current)
        current = prev[current]
    path.append(start)
    path.reverse()

    return path

start = input().strip()
end = input().strip()

result = bfs(start, end)
for num in result:
    print(num)
