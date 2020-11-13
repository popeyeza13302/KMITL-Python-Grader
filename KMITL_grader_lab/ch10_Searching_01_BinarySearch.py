def bi_search(index, lastIndex, array, x):
    if index > lastIndex:   # base case
        return False

    mid = (index+lastIndex)//2      # find middle of array

    if x == array[mid]:             # check middle itself
        return True
    elif x < array[mid]:                             # if x is less than middle
        return bi_search(index, mid-1, array, x)        # recursive left side
    elif x > array[mid]:                             # if x is more than middle
        return bi_search(mid+1, lastIndex, array, x)    # recursive right side

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))