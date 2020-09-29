# week 1
print('*** Fun with countdown ***')
ls = [int(i) for i in input('Enter List : ').split()]
totalList = []
totalGood = []
positionList = []
switch = True
con = False
count = 0
#print(len(ls))
for i in range(len(ls)):
    goodList = []
    #print('loop = ', i)
    #print(switch)
    if ls[i] <= 0:
        continue
    if ls[i] == 1 and switch == True:
        positionList.append(i)
        count += 1
        #print(positionList)
        goodList.append(ls[i])
        totalGood.append(goodList)
        positionList.clear()
        switch = True
        continue
    if i+1 == len(ls):
        break
    else:
        if (ls[i + 1] == 1 and ls[i] != 1) and (con == True or switch == True):
            positionList.append(i)
            positionList.append(i+1)
            count += 1
            #print(positionList)
            for i in positionList:
                goodList.append(ls[i])
            totalGood.append(goodList)
            positionList.clear()
            switch = False
            continue
        if ls[i]-ls[i+1] == 1:
            positionList.append(i)
            switch = False
            con = True
        else:
            positionList.clear()
            switch = True
            con = False

totalList.append(count)
totalList.append(totalGood)
print(totalList)
