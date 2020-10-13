lst = [1, 2, 3]

reversed(lst)
print(lst)

strrr = ' -1'

print(strrr)

num = -100

x = -num

print(x)

for i in range(-5, --1):
    print(i)


def maxDigit():
    # find max Value
    maxNum = 123
    digit = 0
    while maxNum != 0:
        maxNum = maxNum // 10
        digit += 1
    return digit


print(maxDigit())

print(-10 // 10)

data = 123

original = data
print(original)
original = -original
print(original)

print(-28 % 10)

text = 'abcdeedcba'
text1 = 'ab'
print(text[1:-6])
print(text1[0])
print(text1[-1])
print(text1[1:-1])

print('WTF', (2 ** 6) - 1)

print(bin(64))

print('  ')
def DecimalToBinary(num):
    if num >= 2:
        DecimalToBinary(num // 2)
    print(f' num ({num})', end='')
    print(' bin:',num % 2, end='')


DecimalToBinary(2)

print(type(str(10).zfill(5)))

x = 2000000000000000000
print(id(x))
print(id(x))
y=x
print(id(y))

hahah = ['1 2', '3 4']
sour = int(hahah[1].split()[0])
bitter = int(hahah[1].split()[1])

print(sour)
print(bitter)

temp = [7,7,8]
asts = [1,2,3]
x= [asts[1]] + temp
print(x)

thisislist = [1,2,3,4]
thisislist.extend([1,2,3,4])
print(thisislist)


maasdasd = [2]
print(maasdasd[1:])


print(str([1,2,3,4,9,5]))

def testWhileFunc():
    while True:
        print('1')
        return

testWhileFunc()