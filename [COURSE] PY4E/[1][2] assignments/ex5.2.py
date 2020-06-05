# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below:
# Invalid input
# Maximum is 10
# Minimum is 2

largest = None
smallest = None
while True:
    num = input('Enter number:')
    if num == 'done':
        break
    try:
        num_int = int(num)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = num_int
    else:
        if largest < num_int:
            largest = num_int

    if smallest == None:
        smallest = num_int
    else:
        if smallest > num_int:
            smallest = num_int
print('Maximum is', largest)
print('Minimum is', smallest)
