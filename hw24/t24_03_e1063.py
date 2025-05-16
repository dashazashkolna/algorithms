from collections import deque


def count_pieces(grid, m, n):
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                count += 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < m and 0 <= ny < n:
                            if grid[nx][ny] == '#' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

    return count


m, n = map(int, input().split())
grid = []
for _ in range(m):
    row = input().strip()
    grid.append(row)

print(count_pieces(grid, m, n))