# Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def removeChars(str, chars):
    print(str[chars:])

str = 'pynative'

while True:
    chars = input('How many characters to be removed: ')
    try:
        chars = int(chars)
        break
    except:
        print('Wrong input, try again.')
        continue

removeChars(str, chars)
print('Removed', chars, 'characters from', str)
