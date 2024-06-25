def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    else :
        return "Not Found in this array"
    # return -1

arr = [10, 22, 25, 1, 2, 33, 40, 7]
x = 90
print(linear_search(arr, x)) 