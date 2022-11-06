def b_search(array, target, first, last):
    # Loop over the array,first cant > last
    while first <= last:
        # Calculate the mid index
        mid = (first + last) // 2
        # Check in the smaller side of the array
        if array[mid] < target:
            start = mid + 1
            # Check in the bigger parts
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    return 'Not found'
