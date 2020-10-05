def permute(lst, start, end):
    if start == end:
        print('End result',lst)
        return

    for i in range(start, end):
        print('start loop',i, start,' ',end)
        print('swap')
        lst[start], lst[i] = lst[i], lst[start]     # swap
        print(lst)
        print('begin recursive')
        permute(lst, start+1, end)
        print('out of recursive')

        print('backtracking')
        lst[start], lst[i] = lst[i], lst[start]     # backtracking
        print(lst)
        print('end loop',i, start, ' ', end)

permute([1,2,3],0,3)