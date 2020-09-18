def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


num = int(input('Enter Number : '))
print(f'{num}! =', factorial(num))

# if Don't use Recur...

''' 
def factorialNotRecur(number):
    x = 1
    for i in range(1,number+1):
        x *= i
    return x

print(f'{num}! =', factorialNotRecur(num))
'''
