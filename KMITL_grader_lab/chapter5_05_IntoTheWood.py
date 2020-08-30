class Stack:
    """< Default Stack >"""

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of ' + str(self.size()) + ' items : '
        for i in self.items:
            s += str(i) + ' '
        return s

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def empty(self):
        return self.items.clear()

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def reverseStack(old):
    new = Stack()
    while not old.isEmpty():
        new.push(old.pop())  # REVERSE TREE TO MAIN
    return new


inp = input('Enter Input : ').split(',')

stk_tree = Stack()
stk_main = Stack()
stk_see = Stack()

for e in inp:
    e = e.split()
    if e[0] == 'A':
        stk_tree.push(int(e[1]))

    elif e[0] == 'B':
        stk_main = reverseStack(stk_tree)  # REVERSE TREE TO MAIN

        while not stk_main.isEmpty():  # RUN EVERY TREES
            last = stk_main.pop()  # GET LAST_ONE OUT

            stk_tree.push(last)  # PUSH TO TREE

            if stk_see.isEmpty():
                stk_see.push(last)
                continue  # GO ON FOR FIRST_CASE
            elif last < stk_see.peek():
                stk_see.push(last)  # PUSH TO SEE

            elif last >= stk_see.peek():

                while not stk_see.isEmpty() and last >= stk_see.peek():
                    stk_see.pop()
                else:
                    stk_see.push(last)  # PUSH TO SEE
        print(stk_see.size())
        stk_see.empty()

    elif e[0] == 'S':
        stk_main = reverseStack(stk_tree)  # REVERSE TREE TO MAIN
        while not stk_main.isEmpty():
            if stk_main.peek() % 2 == 1:
                stk_tree.push(stk_main.pop() + 2)
            elif stk_main.peek() % 2 == 0 and stk_main.peek() > 0:
                stk_tree.push(stk_main.pop() - 1)
