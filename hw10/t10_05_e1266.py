def duration(N, tracks):
    max_sum = [0]

    def backtrack(index, current_sum):
        if current_sum > N:
            return
        if current_sum > max_sum[0]:
            max_sum[0] = current_sum
        if index == len(tracks) or max_sum[0] == N:
            return

        backtrack(index + 1, current_sum + tracks[index])
        backtrack(index + 1, current_sum)

    backtrack(0, 0)
    return max_sum[0]


try:

    while True:
        line = input().strip()
        if not line:
            break

        parts = list(map(int, line.split()))
        N = parts[0]
        s = parts[1]
        tracks = parts[2:2 + s]

        result = duration(N, tracks)
        print(f"sum:{result}")

except EOFError:
    pass