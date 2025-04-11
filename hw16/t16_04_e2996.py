import sys


def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())

    subordinates = [[] for _ in range(N + 1)]
    bribes = [0] * (N + 1)

    for i in range(1, N + 1):
        parts = list(map(int, sys.stdin.readline().split()))
        bribes[i] = parts[0]
        if parts[1] > 0:
            subordinates[i] = parts[2:2 + parts[1]]

    memo = {}

    def dp(u):
        if u in memo:
            return memo[u]

        if not subordinates[u]:
            memo[u] = bribes[u]
            return bribes[u]

        min_total = float('inf')
        for v in subordinates[u]:
            current = bribes[u] + dp(v)
            if current < min_total:
                min_total = current

        memo[u] = min_total
        return min_total

    print(dp(1))
    

if __name__ == "__main__":
    main()