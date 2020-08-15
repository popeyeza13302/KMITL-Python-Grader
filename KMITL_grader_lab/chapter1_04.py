def odd_list(al):
    List = al
    newList = list()
    for i in range(len(List)):
        if List[i] %2 != 0:
            newList.append(List[i])
    return newList

    # เติมส่วนของคำสั่ง



print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
#print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)