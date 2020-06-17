# Question 3: Given a string, display only those characters which are present at an even index number.

def evenIndexNum(str):
    print('Original String is', str)
    print('Printing only even index chars')
    for each in range(0, len(str)-1, 2):
        print('index[',each,']', str[each])

word = 'pynative'
evenIndexNum(word)
