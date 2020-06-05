# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
#
# The basic outline of this problem is to read the file, look for integers using the re.findall(),
# looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
file = open('regex_sum_551277.txt')

count = 0
for line in file:
    find_numbers = re.findall('[0-9]+', line) #find any number in each line of the file, greedy-wise. (and puts it/them in a list)
    for each in find_numbers:
        count = count + int(each)
print(count)
