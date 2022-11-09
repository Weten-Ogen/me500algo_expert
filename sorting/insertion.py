"""
    Insertion sort 
    :array -> str ( return a sorted list)
    
"""
def insertion(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

arr = [55,43,3,2,7,4,2,1,18,45,13]
print(insertion(arr))