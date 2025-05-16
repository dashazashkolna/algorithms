from collections import deque


def find_path(n, grid):
    start = None
    end = None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j] == 'X':
                end = (i, j)

    if not start or not end:
        return None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            path = []
            current = end
            while current != start:
                path.append(current)
                current = parent[current[0]][current[1]]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and grid[nx][ny] in ('.', 'X'):
                    visited[nx][ny] = True
                    parent[nx][ny] = (x, y)
                    queue.append((nx, ny))

    return None


def mark(grid, path):
    new_grid = [row.copy() for row in grid]

    for x, y in path:
        if new_grid[x][y] in ('.', 'X'):
            new_grid[x][y] = '+'
        if (x, y) == path[0]:
            new_grid[x][y] = '@'

    return new_grid


if __name__ == '__main__':
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]

    path = find_path(n, grid)

    if not path:
        print("N")
    else:
        print("Y")
        new_grid = mark(grid, path)
        for row in new_grid:
            print(''.join(row))