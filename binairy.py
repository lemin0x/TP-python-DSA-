def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    arr.sort()  # Ensure the array is sorted

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [10, 22, 25, 1, 2, 33, 40, 7]
x = 25
print(binary_search(arr, x))  # Output: 4 (after sorting)
