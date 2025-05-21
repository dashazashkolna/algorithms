def count_members(heights, a, b):
    count = 0
    for height in heights:
        if a <= int(height) <= b:
            count += 1
    return count


with open('input.txt') as f:
    while True:
        n = f.readline()
        if not n:
            break
        heights = list(f.readline().split())

        limits = list(f.readline().split())
        a, b = int(limits[0]), int(limits[1])

        print(count_members(heights, a, b))

