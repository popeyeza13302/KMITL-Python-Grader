# week 2
string = input('Enter String : ')


def mapping(str):
    listCharacter = []
    listNumber = []
    position = 0
    for i in range(len(str)):

        for j in range(len(listCharacter)):
            if listCharacter[j] == str[i]:
                listNumber.append(listNumber[j])
                break
        else:
            listNumber.append(position)
            position += 1

        listCharacter.append(str[i])

    return listNumber


print(mapping(string))
