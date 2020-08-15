class funString:
    store = ''

    def __init__(self, str, num):
        self.str = str

        if num == 1:
            x = self.stringLength()
        if num == 2:
            x = self.upperLowerCase()
        if num == 3:
            x = self.reverseString()
        if num == 4:
            x = self.sameCharactor()

        print(x)


    def stringLength(self):
        return len(self.str)

    def upperLowerCase(self):

        for i in range(len(self.str)):
            str_num = ord(self.str[i])
            if 65 <= str_num <= 90:
                str_num += 32
            elif 97 <= str_num <= 122:
                str_num -= 32
            self.store += chr(str_num)
        return self.store

    def reverseString(self):
        return self.str[::-1]

    def sameCharactor(self):
        for i in range(len(self.str)):
            if(self.str[i] not in self.store):
                self.store += self.str[i]
        return self.store
'''
        for i in range(-1,-len(self.str)-1,-1):
            self.store += self.str[i]
'''


string, numb = input("Enter String and Number of Function : ").split()
number = int(numb)

obj = funString(string, number)