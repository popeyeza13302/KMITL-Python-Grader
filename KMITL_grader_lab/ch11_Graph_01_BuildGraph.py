inputlst = input('Enter : ').split(',')

lst = []
for i in inputlst:  # split
    i = i.split()
    for k in range(2):  # for first word and second word
        if i[k] not in lst:     # if word not in lst
            if len(lst) == 0:       # init word
                lst.append(i[k])
            else:
                for j in range(len(lst)):   # check who come first
                    if i[k] < lst[j]:
                        lst.insert(j, i[k])
                        break
                else:
                    lst.append(i[k])    # insert last word

# A B,A C,C D,D B
matrix = [[0 for i in range(len(lst))] for i in range(len(lst))]

for i in inputlst:
    i = i.split()
    start = lst.index(i[0])     # get index row
    end = lst.index(i[1])       # get index col
    matrix[start][end] = 1     # place value, only '1'

print('   ', '  '.join(lst))
for i, row in enumerate(matrix):
    print(f'{lst[i]} :', ', '.join(map(str, row)))  # map int to str and print as row
