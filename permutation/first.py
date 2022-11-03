def permutate(string:str, pock=''):
    # If the string is empty
    if len(string) == 0:
        # return an empty string
        print(pock)
    else:
        # Loop through the string
        for i in range(len(string)):
            # holds the current letter
            letter = string[i]
            # all characters before the current
            front =  string[0:i]
            #  all letters after the current
            back = string[i + 1:]
            #  add to form new string
            together = front + back
            #  call the function recursively
            permutate(together, letter + pock)

permutate('AB', '')