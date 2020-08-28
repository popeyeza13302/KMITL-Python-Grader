class stack:
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

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def match(open, close):
    op = '(['
    cl = ')]'
    return op.index(open) == cl.index(close)


lst = input('Enter Input : ')
stack_paren = stack()
stack_left = stack()

for paren in lst:
    if paren in '([':
        stack_paren.push(paren)

    elif paren in ')]':
        if stack_paren.isEmpty():          # close left
            stack_left.push(paren)
            continue

        if not match(stack_paren.peek(), paren):  # open , close
            stack_left.push(stack_paren.pop())  # keep open to left
            stack_left.push(paren)  # keep close to left
        else:
            stack_paren.pop()  # throw open out

while not stack_paren.isEmpty():            # open left
    stack_left.push(stack_paren.pop())

print(stack_left.size())
if stack_left.size() == 0:
    print('Perfect ! ! !')
