# Question 1:
# Accept two integer numbers from a user and return their product and  if the product is greater than 1000, then return their sum

# MY SOLUTION #
def math(x, y): #A def doing the actual math problem
    sum = num1 * num2
    if sum > 1000:
        print(num1 + num2)
    else:
        print(sum)

while True: #A loop in case the input is wrong or not a number
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        break
    except:
        print('Wrong input, use numbers.')

result = math(num1, num2)



# # SOLUTION PROPOSED ##
# def multiplication_or_sum(num1, num2):
#   product = num1 *num2
#   if(product <= 1000):
#     return product
#   else:
#     return num1 +num2
#
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# result = multiplication_or_sum(number1, number2)
# print("The result is", result)
