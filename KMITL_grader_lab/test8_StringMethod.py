inp = [str(c) for c in input('Enter text : ')]
# sirawit SUKWATtanavit
print(inp)

gap = ord('a')-ord('A')

def upperString(lst):
    text = ''
    for i in lst:
        if 'a' <= i <= 'z':
            text += chr(ord(i)-gap)
        else:
            text += i
    print(text)
    return text

def lowerString(lst):
    text = ''
    for i in lst:
        if 'A' <= i <= 'Z':
            text += chr(ord(i) + gap)
        else:
            text += i
    print(text)
    return text

def capitalize(lst):
    text = ''
    for loop, i in zip(range(len(lst)), lst):
        if loop == 0:
            if 'a' <= i <= 'z':
                text += chr(ord(i) - gap)
            else:
                text += i
        else:
            if 'A' <= i <= 'Z':
                text += chr(ord(i) + gap)
            else:
                text += i
    print(text)
    return text


upperString(inp)
lowerString(inp)
capitalize(inp)

text = ''.join(inp)
text = 'sadasdASDASDASD'

print(text.capitalize())
print(text.islower())
print(upperString(inp).isupper())