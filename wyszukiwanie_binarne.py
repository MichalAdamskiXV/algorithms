arr = [2,5,7,8,9,14,16,17,38,58,69]

def binary_search(arr, n, target):
    l = 0
    r = n-1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            return  mid
        elif arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1

print(binary_search(arr, len(arr), 17))