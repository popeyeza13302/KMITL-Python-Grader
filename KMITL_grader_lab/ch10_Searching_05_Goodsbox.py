# thanks to Qirals, I'm fucking gave up
# brute force
def minimumWeight(lst, box):
    if box == 1:    # base case
        return sum(lst)

    minWeight = 99999  # init new min weight (infinity+++)
    for index in range(len(lst)):   # loop all index // find all possible way to push in the box...

        if len(lst[index:]) < box-1:    # if len of goods less than all box
            break

        leftValue = sum(lst[:index])    # [,i) # sum of my box (left side)
        rightValue = minimumWeight(lst[index:], box - 1)  # [i,) # recursive go to next box (right side)

        minWeight = min(max(leftValue, rightValue), minWeight)  # find lowest of sum of every set of box

    return minWeight


weightlst, k = input('Enter Input : ').split('/')
k = int(k)
weightlst = [int(i) for i in weightlst.split()]

ans = minimumWeight(weightlst, k)
print(f'Minimum weigth for {k} box(es) = {ans}')