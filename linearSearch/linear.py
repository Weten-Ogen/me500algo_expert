def l_search(array, target):
    # Go through all the array
    for i in range(len(array)):
        # If an item matches target
        if array[i] == target:
            return 'Found'
        else:
            return 'Not Found'

print(l_search(['marcus','blessing', 'alice', 'asneth', 'oware', 'gideon'], 'marcus'))