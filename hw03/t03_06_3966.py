def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


n = int(input())
collection = list(map(int,input().split()))

m = int(input())
check = list(map(int, input().split()))
for x in check:
    if binary_search(collection, x):
        print("YES")
    else: print("NO")