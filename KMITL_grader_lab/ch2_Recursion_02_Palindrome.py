def palindrome(text):
    if len(text) == 1:  # base case 1st
        return
    elif len(text) == 2 and text[0] == text[-1]:   # base case 2nd
        return
    elif text[0] == text[-1]:
        return palindrome(text[1:-1])   # get only inside of string ... and run it's self again
    else:
        return False    # not a palindrome


inp = input('Enter Input : ')

result = palindrome(inp)
if result is False:
    print(f'\'{inp}\'', 'is not palindrome')
else:
    print(f'\'{inp}\'', 'is palindrome')
