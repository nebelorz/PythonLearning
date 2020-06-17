# Question 2: Given a range of first 10 numbers, iterate from start number to the end number and print the sum of the current number and previous number

# MY SOLUTION #
current_number = 0
previous_number = 0
range = range(10)

for each in range:
    current_number = each
    sum_numbers = current_number + previous_number
    print('Current number', current_number, 'Previous number', previous_number, 'Sum:', sum_numbers)
    previous_number = current_number



# # SOLUTION PROPOSED ##
# def sumNum(num):
#     previousNum = 0
#     for i in range(num):
#         sum = previousNum + i
#         print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
#         previousNum = i
#
# print("Printing current and previous number sum in a given range(10)")
# sumNum(10)


# =========================================================================== #
# What I've learnt:
# I have to create functions (def) to do the calculations of the problem, though it's not going to be repeated.
