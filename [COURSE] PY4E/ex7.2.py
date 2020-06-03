# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

line_count = 0
total_value = 0

file_name = input('Enter file name:')
if len(file_name) < 1 :
    file_name = "mbox-short.txt"
file = open(file_name)

# Finding position of the value (21)
# text = 'X-DSPAM-Confidence:    0.8475'
# text_number = text.find('0')
# print(text_number)

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        line_count = line_count + 1
        try:
            value = float(line[21:]) #From 21 (not including) until the end.
            total_value = value + total_value
        except:
            print('Something went wrong.')
            quit()
print('Average spam confidence:', total_value / line_count)
