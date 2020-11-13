def greaterThan(index, array, x):
    if index > len(array) - 1:              # base case
        return 'No First Greater Value'

    if array[index] <= x:
        return greaterThan(index + 1, array, x)     # recursive go to next index and return value back
    elif array[index] > x:                  # FOUND!!!
        return array[index]                         # return value greater than


inputlst, xlst = input('Enter Input : ').split('/')
inputlst = [int(i) for i in inputlst.split()]
xlst = [int(i) for i in xlst.split()]

inputlst.sort()     # must sorted becuz ez to find with this algorithm

for i in xlst:
    print(greaterThan(0, inputlst, i))  # insert left lst and right lst
