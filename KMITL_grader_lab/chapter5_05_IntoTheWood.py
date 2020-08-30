class Stack:
    """< Default Stack >"""

    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

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
        new.push(old.pop())  # REVERSE STACK
    return new


inp = input('Enter Input : ').split(',')

stk_tree = Stack()      # WE HAVE 3 STACKS
stk_main = Stack()
stk_see = Stack()

for e in inp:
    e = e.split()
    if e[0] == 'A':
        stk_tree.push(int(e[1]))    # PUSH NUM TO TREE

    elif e[0] == 'B':
        stk_main = reverseStack(stk_tree)  # REVERSE TREE TO MAIN

        while not stk_main.isEmpty():   # RUN EVERY TREES
            last = stk_main.pop()           # GET LAST_ONE OUT
            stk_tree.push(last)             # PUSH BACK TO TREE

            if stk_see.isEmpty():           # CHECK IF FIRST ONE (JUST THROW IN)
                stk_see.push(last)
                continue                    # SKIP

            elif last < stk_see.peek():     # I'M SMALLER THAN YOU
                stk_see.push(last)              # THROW TO SEE

            elif last >= stk_see.peek():    # I'M BIGGER THAN YOU
                while not stk_see.isEmpty() and last >= stk_see.peek():  # LOOP UNTIL I'M SMALLER THAN YOU
                    stk_see.pop()           # DELETE OUT
                else:
                    stk_see.push(last)          # PUSH TO SEE

        print(stk_see.size())               # PRINT CAN SEE
        stk_see.empty()                     # DELETE STACK OF SEE

    elif e[0] == 'S':
        stk_main = reverseStack(stk_tree)   # REVERSE TREE TO MAIN

        while not stk_main.isEmpty():       # RUN EVERY TREES
            if stk_main.peek() % 2 == 1:
                stk_tree.push(stk_main.pop() + 2)                   # ODD +2
            elif stk_main.peek() % 2 == 0 and stk_main.peek() > 0:
                stk_tree.push(stk_main.pop() - 1)                   # EVEN -1 (BUT GREATER THAN 0)
