#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(a,b,c):
    if c == True:
        x = (a**2 + b**2)
        x = math.sqrt(x)
        return x
    elif c == False:
        if a > b:
            x = (a**2 - b**2)
            x = math.sqrt(x) 
            return x
        elif b > a:
            x = (b**2 - a**2)
            x = math.sqrt(x) 
            return x