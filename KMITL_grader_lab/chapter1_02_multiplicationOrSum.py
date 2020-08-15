print('*** multiplication or sum ***')
#x, y = input('Enter num1 num2 : ').split()
x, y = map(int, input('Enter num1 num2 : ').split())
product = x*y
sum = x+y

if product > 1000:
    print('The result is', sum)
else:
    print('The result is', product)