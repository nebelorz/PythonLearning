# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def divisibleBy5(list):
    for each in list:
        if each % 5 == 0:
            print(each)
        else:
            continue

numbers = [10, 20, 33, 46, 55]
print('Given list is', numbers)
print('Divisible of 5 in this list:')
divisibleBy5(numbers)
