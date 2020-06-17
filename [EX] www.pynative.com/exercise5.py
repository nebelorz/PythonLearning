# Question 5: Given a list of numbers, return True if first and last number of a list is same
import time

def same_numbers(list):
    print('Given list is:', list)
    if list[0] == list[-1]:
        return True
    else:
        return False

list_of_numbers = list()
print('Enter numbers, when you are done write "done".\n')
while True:
    inp = input('Enter numbers: ')
    if inp == 'done':
        break
    try:
        number = int(inp)
        list_of_numbers.append(number)
        continue
    except:
        print('You have entered a wrong character, please use only numbers.')
        continue

print('Result is:', same_numbers(list_of_numbers))
