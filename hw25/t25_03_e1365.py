import heapq


def short_way(n, s, f, matrix):
    dist = [float('inf')] * n
    dist[s] = 0
    queue = [(0, s)]

    while queue:
        curr_dist, u = heapq.heappop(queue)
        if curr_dist > dist[u]:
            continue
        for v in range(n):
            weight = matrix[u][v]
            if weight != -1 and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(queue, (dist[v], v))

    return dist[f] if dist[f] != float('inf') else -1


n, s, f = map(int, input().split())
s -= 1
f -= 1
matrix = [list(map(int, input().split())) for _ in range(n)]

print(short_way(n, s, f, matrix))
