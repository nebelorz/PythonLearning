# Question 7: Return the total count of string “Emma” appears in the given string
# Given string is “Emma is good developer. Emma is a writer”

def findEmma(text):
    count = 0
    text_split = text.split()
    for each in text_split:
        if 'Emma' in each:
            count += 1
    print('Emma appeared', count, 'times.')

string = 'Emma is good developer. Emma is a writer'
findEmma(string)

## I have learned a new function, count().
## This way I haven't to do a split and iterate through all the items in the list:
# sampleStr = "Emma is good developer. Emma is a writer"
# cnt = sampleStr.count("Emma")
# print(cnt)
