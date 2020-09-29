class stack:

    def __init__(self, lst = None):
        if lst == None:
            self.item = []
        else:
            self.item = lst

    def __str__(self):
        s = ''
        for i in self.item:
            s += str(i) + ' '
        return s

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]


def infixToPostFix(equation):
    result = ''
    priority = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0}
    stk = stack()

    for i in equation:
        if i in '(':
            stk.push(i)

        elif i in '^*/%+-':
            if stk.isEmpty():
                stk.push(i)
                continue

            if priority[stk.peek()] < priority[i]:
                stk.push(i)
            else:
                while not stk.isEmpty() and stk.peek() != '(':
                    result += stk.pop()
                stk.push(i)

        elif i in ')':
            while stk.peek() != '(':
                result += stk.pop()
            else:
                stk.pop()       # get paren open out
        else:
            result += i

    while not stk.isEmpty():     # get the last operation out of stack
        result += stk.pop()

    return result


infix = input('insert equation : ')
# a+b*c-(d/e+f)*g
print(infix)
print(infixToPostFix(infix))







