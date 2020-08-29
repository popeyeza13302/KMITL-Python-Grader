class Stack:
    """< Default Stack >"""

    def __init__(self, list=None):
        if list == None:
            self.weight = []
            self.sound = []
        else:
            self.weight = list
            self.sound = list

    def __str__(self):
        s = 'stack of ' + str(self.size()) + ' items : '
        for i in self.weight:
            s += str(i) + ' '
        return s

    def push(self, i, j):
        self.weight.append(i)
        self.sound.append(j)

    def pop(self, x):
        if x == 0:
            return self.weight.pop()
        elif x == 1:
            return self.sound.pop()

    def peek(self, x):
        if x == 0:
            return self.weight[-1]
        elif x == 1:
            return self.sound[-1]

    def isEmpty(self):
        return len(self.weight) == 0

    def size(self):
        return len(self.weight)


lst = input("Enter Input : ").split(',')
# 1 10,5 20,3 30,3 40,4 50

lst_plate = []

for i in lst:
    lst_plate.append(tuple(i.split()))

stk_plate = Stack()
break_plate = Stack()

for i, j in lst_plate:
    if stk_plate.isEmpty():
        stk_plate.push(int(i), int(j))
    else:
        while not stk_plate.isEmpty() and stk_plate.peek(0) < int(i):
            stk_plate.pop(0)
            print(stk_plate.pop(1))
        stk_plate.push(int(i), int(j))


