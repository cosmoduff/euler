# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
"""
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def define_number(x):
# Defines a number as digit ten hundred or thousand
    
    type = ""

    if len(str(x)) == 1:
        type = "digit"
    elif len(str(x)) == 2:
        type = "ten"
    elif len(str(x)) == 3:
        type = "hundred"
    elif len(str(x)) == 4:
        type = "thousand"
    else:
        print("The number can not be defined")

    return type

print(define_number(10200))
