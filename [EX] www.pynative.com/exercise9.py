# Question 9: Reverse a given number and return true if it is the same as the original number

def reverseNumber(number):
    length = len(number)
    reverse_number = number[length :: -1]
    print('Input number is:', number)
    print('Reversed number is:', reverse_number)
    if reverse_number == number:
        return True
    else:
        return False

inp = input('Enter a number:')
print('The original and reversed number are the same:', reverseNumber(inp))




## Learnt that only with a slicing and the length, I can reverse a string.
