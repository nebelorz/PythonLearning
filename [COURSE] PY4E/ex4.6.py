# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

# Function starts.
def computepay(hfl, rfl):
    # If hours input is less than 0, then quit.
    if hfl < 0:
        return 'Hours cannot be less than 0.'
        quit()
    elif hfl <= 40:
        npay = hfl * rfl
        return npay
    elif hfl > 40:
        npay = hfl * rfl
        xhfl = hfl - 40
        xrfl = rfl * 0.5
        xpay = xhfl * xrfl
        return xpay + npay
    # This else is just in case an error occurs.
    else:
        print('Something went wrong.')
        quit()
# Function ends.
hours = input('Enter hours:')
rate = input('Enter rate:')
try:
    hfl = float(hours)
    rfl = float(rate)
except:
    print('Wrong input on hours/rate, try again.')
    quit()
totalpay = computepay(hfl,rfl)
print('Pay', totalpay)
