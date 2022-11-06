def bubble(arr):
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) -i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, iterations
arr = [46,5,7,8,100,34,2,55,7,3,90,1]
print(bubble(arr))
