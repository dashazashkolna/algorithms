from collections import deque


def wave(start, matrix):
    distances = [-1] * len(matrix)
    distances[start] = 0

    queue = deque()
    queue.append(start)
    while queue:
        current = queue.popleft()
        for u in range(len(matrix)):
            if matrix[current][u] == 1 and distances[u] == -1:
                queue.append(u)
                distances[u] = distances[current] + 1

    return distances


n, x = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

res = wave(x - 1, matrix)
print(*res)
