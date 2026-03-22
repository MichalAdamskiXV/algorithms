arr = [3,6,1,8,9,2,7,1,6,8,31,64,12,54,34,12]

def bubble_sort(arr, n):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(arr, len(arr)))