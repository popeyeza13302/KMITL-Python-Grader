lst = [int(i) for i in input('Enter Input : ').split()]

for loop in range(1, len(lst)):   # amount of outer loop ... 1 to length of lst
    moveNum = None      # init move Number
    swap = False        # init swap state

    for i in range(len(lst) - loop):  # index 0 to length - 1(loop)..(default)
        if lst[i] > lst[i + 1]:                     # if before > after
            moveNum = lst[i]                            # stored move Number
            lst[i], lst[i + 1] = lst[i + 1], lst[i]     # swap !
            swap = True                                 # swap true

    if loop <= len(lst) - 1 and swap is False:          # no swapping... ascending order already
        print('last step :', lst, f'move[{moveNum}]')      # (forced to last case)
        break
    elif loop == len(lst) - 1:                          # run every single number (natural last case)
        print('last step :', lst, f'move[{moveNum}]')
    else:                                               # normal case (in progress)
        print(f'{loop} step :', lst, f'move[{moveNum}]')
