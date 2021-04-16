#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(a,b):
    x = a[0]
    y = a[1]
    x1 = b[0]
    y1 = b[1]
    c = ((x1 - x)**2 + (y1 - y)**2)
    c = math.sqrt(c)
    return c
