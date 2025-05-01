# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

a = [1,2,3,4,5]

def even(a):
    return a % 2 == 0


# filter return an object. 
b = filter(even, a)
print(list(b))

# Map : The map() function is used to apply a given function to every item of an iterable, such as a list or tuple, and returns a map object (which is an iterator).
# Map function also return a list of object.
li = [1,2,3,4,5]
print(list(map(lambda x: x*2, li)))

# Reduce : The reduce() function in Python applies a function cumulatively to the items of an iterable, from left to right, to reduce the iterable to a single value. It is part of the functools module and requires importing before use. 

from functools import reduce 
print(reduce(lambda x,y: x*y, li))
