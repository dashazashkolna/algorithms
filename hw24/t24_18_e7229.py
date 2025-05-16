from collections import deque


def max_coins(N, M, K, grid):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    coin_indices = {}
    coin_id = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                coin_indices[(i, j)] = coin_id
                coin_id += 1

    queue = deque()
    start_mask = 0
    if (0, 0) in coin_indices:
        start_mask |= 1 << coin_indices[(0, 0)]

    # BFS: (x, y, time, mask)
    queue.append((0, 0, 0, start_mask))
    visited = set()
    visited.add((0, 0, start_mask))

    max_collected = -1

    while queue:
        x, y, t, mask = queue.popleft()
        if t > K:
            continue

        if (x, y) == (N - 1, M - 1):
            max_collected = max(max_collected, bin(mask).count('1'))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 1:
                new_mask = mask
                if (nx, ny) in coin_indices:
                    coin_bit = 1 << coin_indices[(nx, ny)]
                    new_mask |= coin_bit
                state = (nx, ny, new_mask)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, t + 1, new_mask))

    return max_collected if max_collected != -1 else -1


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(max_coins(N, M, K, grid))