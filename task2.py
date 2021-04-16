#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest (list):
    length = len(list)
    list.sort()
    largest = list[length - 1]
    return largest