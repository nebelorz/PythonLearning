# Question 10: Given a two list of numbers create a new list such that new list
# should contain only odd numbers from the first list and even numbers from the second list
# First List  [10, 20, 23, 11, 17]
# Second List  [13, 43, 24, 36, 12]
# result List is [23, 11, 17, 24, 36, 12]

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
merged_list = []

def mergeList(list1, list2):
    for num in list1:
        if (num % 2) == 0:
            continue
        else:
            merged_list.append(num)
    for num in list2:
        if (num % 2) == 0:
            merged_list.append(num)
        else:
            continue

mergeList(list1, list2)
print('The merged list is:')
print(merged_list)
