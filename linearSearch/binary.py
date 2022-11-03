def b_search(array, target, first, last):
    # Loop over the array,first cant > last
    while first <= last:
        # Calculate the mid index
        mid = (first + last) // 2
        # Check in the smaller side of the array
        if array[mid] < target:
            b_search(array, target, first, mid)
            # Check in the bigger parts
        elif array[mid] > target:
            b_search(array, target, mid + 1, last)
        else:
            return 'found'
    return 'Not found'
