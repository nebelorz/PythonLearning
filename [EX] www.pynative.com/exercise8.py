# Question 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for each in range(1,6):
    for number in range(each):
        print(each, end='')
    print('\n')
