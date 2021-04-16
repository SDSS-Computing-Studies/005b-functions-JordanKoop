#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""
def factors(x):
    num = []
    a=1
    num.insert(0,x)
    while a < x:
        if x % a == 0:
            num.insert(0,a)
            a = a + 1
        else:
            a = a + 1
    num.sort()
    return num