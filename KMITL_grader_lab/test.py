lst = [1,2,3]

reversed(lst)
print(lst)

strrr = ' -1'

print(strrr)


num = -100

x = -num

print(x)

for i in range(-5,--1):
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

print(-10//10)


data = 123

original = data
print(original)
original = -(original)
print(original)

print(-28%10)