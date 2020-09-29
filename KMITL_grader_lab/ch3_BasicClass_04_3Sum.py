# week 2
array = [int(i) for i in input('Enter Your List : ').split()]

sum = 0

totalList = []

if (len(array) < 3):
    print('Array Input Length Must More Than 2')
else:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                sum = array[i] + array[j] + array[k]
                if sum == 0:

                    tempList = [array[i], array[j], array[k]]
                    if tempList not in totalList:
                        totalList.append(tempList)

                    #old location
    print(totalList)
