def twobit(index, number):
    # until it exceed the last one
    if index == number:
        print(total)    # print result
        return

    # assign to 0 to first
    total[index] = 0

    # go deeper
    twobit(index + 1, number)
    # if finish 0 next go to 1

    # assign to 1 to second
    total[index] = 1

    # go deeper
    twobit(index + 1, number)
    # if finish 1 ... return to upper
    return


inpNum = int(input('Enter Num : '))

total = [0] * inpNum  # [0,0,0,0]
twobit(0, inpNum)
