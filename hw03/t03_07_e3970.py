def bisect_left(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left


def bisect_right(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return left


def count_color(colors, target):
    left = bisect_left(colors, target)
    right = bisect_right(colors, target)
    return right - left


n = int(input())
collection = list(map(int,input().split()))
m = int(input())
check = list(map(int, input().split()))

for x in check:
    print(count_color(collection, x))