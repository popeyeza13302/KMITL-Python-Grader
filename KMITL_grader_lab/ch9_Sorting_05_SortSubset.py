def bubbleSortLength(subList):
    for loop in range(1, len(subList)):
        swap = False

        for i in range(len(subList) - loop):
            if len(subList[i]) > len(subList[i + 1]):
                # swapping len of subset
                subList[i], subList[i + 1] = subList[i + 1], subList[i]
                swap = True

        if swap is False:
            break
    return subList


def bubbleSortNum(subList):
    for loop in range(1, len(subList)):
        swap = False

        for i in range(len(subList) - loop):
            if subList[i] > subList[i + 1]:
                # swapping num of subset
                subList[i], subList[i + 1] = subList[i + 1], subList[i]
                swap = True

        if swap is False:
            break
    return subList


# korn code - knapsack
def subListSum(ans, lst, index=0, result=None, carry=None):  # knapsack style

    if result is None:  # init new list
        result = []
    if carry is None:
        carry = []

    if index >= len(lst):    # base case    # increasing to exceed len(lst)
        #print(carry)
        return result

    carry.append(lst[index])
    #print('assign Value', result, '===',carry, index)

    if sum(carry) == ans:   # sum of lst ... compare to answer
        result.append(carry.copy())     # copy because it pass by ref ...

    result = subListSum(ans, lst, index + 1, result, carry)  # recursive
    #print()
    #print('after recur1', result, '===', carry, index)
    carry.pop()
    #print('pop before recur2', result, '===', carry, index)
    #print()
    result = subListSum(ans, lst, index + 1, result, carry)  # recursive
    #print()
    #print('after recur2', result, '===', carry, index)
    #print()
    return result


ans, lst = input('Enter Input : ').split('/')
ans = int(ans)
lst = [int(i) for i in lst.split()]

subList = []

# 2/-2 3 1 -1 0 -3 2
lst = bubbleSortNum(lst)
subList = subListSum(ans, lst)

# print(subList)
if len(subList) != 0:
    for i in bubbleSortLength(subList):
        print(i)
else:
    print('No Subset')

'''
def binaryNum(lstNum, binary, index):
    sum = 0
    tempList = []
    if index == -1:  # base case
        return sum, tempList

    sum, tempList = binaryNum(lstNum, binary, index - 1)

    if binary[index] == '1':
        sum += lstNum[index]
        tempList.append(lstNum[index])

    return sum, tempList
'''

'''
for i in range(2 ** len(lst)):
    stringBinary = str(bin(i)).replace('0b', '').zfill(len(lst))
    result, resultList = binaryNum(lst, stringBinary, len(lst) - 1)
    if result == ans:
        subList.append(resultList)
'''
