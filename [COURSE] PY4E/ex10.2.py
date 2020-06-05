# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

file_name = input('Enter file name:')
if len(file_name) < 1:
    file_name = 'mbox-short.txt'
file = open(file_name)

dictionary = dict()
list = list()
for line in file:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        line_split = line.split()
        time_split = line_split[5].split(':') #splitting the hour/minutes/seconds directly
        dictionary[time_split[0]] = dictionary.get(time_split[0], 0) + 1 #taking only the hour value and adding it

# #Those two lines will do the same as the code below them, its a little more complex to read, but cleaner (using this I also can remove the list from the code)
# for k,v in sorted(dictionary.items()):
#     print(k,v)

for each in dictionary.items():
    list.append(each)
    list = sorted(list)

for k,v in list:
    print(k,v)
