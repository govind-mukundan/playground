

# Modules
# import helps with importing all or specific symbols from another module
import sys
import sys as huh   # an alias here
from pprint import pprint


# Function
def my_func(p0, p1, p2 = " --- "):
    assert type(p0) is str
    assert type(p1) is str
    assert type(p2) is str
    
    print p0 + p2 + p1


print "This is the default module search path:"
pprint(sys.path)
pprint(huh.path)

# A package is just a directory that stores python files aka modules

# Command line arguments are available in sys.argv
print len(sys.argv)
print sys.argv[0] # The first argument is the path of this file

# Types
x = float(1)      # same as x = 1.0, other constructors are int(), long(), complex()
assert type(x) is float   # double does not exist as float is implemented as double

# Deleting Variables from scope
test = "govind"
print test
del test
# print test    ERROR
my_func("govind", "mukundan")
my_func(p1 = "end", p0 = "begin")
result = my_func(p1 = "end", p0 = "begin", p2 = "****")
print result   # Implicit return value of None

## LOOPS
# Iterate over all the elements
l = range(3, 10)
for x in l:
    print x

if all(l):
    print("All elements of this list are TRUE")

if any(l):
    print("ANY element of this list is TRUE")

d = {}
assert type(d) is dict
# Iterate over all elements and also get their index
# This is an alternative to: for i in range(len(l))
for i,x in enumerate(l):
    print (i,x)
    d["key_" + str(i)] = x    # Adding elements to s dictionary

# Tuples are immutable
tup = ((1,2), (20, 30))
print(tup)

## LIST COMPREHENSION
# Transform the int list elements to string elements
ls = [str(x) for x in l]

## GENERATORS


## ASSERTIONS
assert hasattr(l, "__iter__")
assert type(l) is list, 'Strange Type'
# `rank_test`: Test cell
print("{}. {}: {}".format(l, d, "This is print"))
# IS does not check value, so you cannot use: tup is ((1,2), (20, 30))
assert type(tup) is tuple and tup == ((1,2), (20, 30))








    
