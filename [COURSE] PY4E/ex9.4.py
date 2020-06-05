# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

file_name = input('Enter file name:')
if len(file_name) < 1:
    file_name = 'mbox-short.txt'
file = open(file_name)

dictionary = dict()
for line in file:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        #This code works, but the one used is more compact
        #line_split = line.split()
        #email = line_split[1]
        #dictionary[email] = dictionary.get(email, 0) + 1
        dictionary[line.split()[1]] = dictionary.get(line.split()[1], 0) + 1
#print(dictionary)
count = None
email = None
for k,v in dictionary.items():
    if email == None or v > count:
        email = k
        count = v
print(email,count)
