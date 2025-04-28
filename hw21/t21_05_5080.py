n = int(input())
k = 0
for x in range(n):
    row = list(map(int,input().split()))
    if sum(row) == 1:
        k += 1

print(k)