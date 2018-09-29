

## Modules
# import helps with importing all or specific symbols from another module
import sys
import sys as huh   # an alias here
from pprint import pprint


## Function
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

## DICT
d = {}
assert type(d) is dict

# Iterate over all elements and also get their index
# This is an alternative to: for i in range(len(l))
for i,x in enumerate(l):
    print (i,x)
    d["key_" + str(i)] = x    # Adding elements to s dictionary
	
d.items()	# can be used to serialize the dictionary as a LIST of TUPLES
# This is useful when applying transformations to the dict elements

# Default values for missing keys
if key in some_dict:
	value = some_dict[key]
else:
	value = default_value

# Can be replaced with 
value = some_dict.get(key, default_value)

# Normal dicts have 2 different operations for initializing an entry and updating it, i.e.
d["name"] = "Govind"  			# creates a new entry
d["name"].append(" Mukundan")  	# Updating an existing entry
# To avoid having to check if the key exists or not before updating it, you can use a defaultdict
# which takes an init function that will be called when creating a new entry


# Tuples are IMMUTABLE
tup = ((1,2), (20, 30))
print(tup)




## SETS
# Sets always have unique elements (no duplicates)
# So a simple way to discard duplicates from a list is to make a set out of it
# empty set
s = set()
# add to set
s = s.union(set{['govind'])

## USEFUL BULITINS
# in === .contains()
# len(x) === .len()
# collection.count(value) === Counts the number of times a value appears
# collection.index(value) === indexof

def some_condition(x):
	return True

## LIST/DICT/SET COMPREHENSION

# Transform the int list elements to string elements
ls = [str(x) for x in l if some_condition(x)]  # Creates a LIST
s = {str(x) for x in l if some_condition(x)}   # Creates a SET
d = {str(x):x for x in l if some_condition(x)} # Creates a DICT
# These are equivalent to map(), filter() and/or loops. They are not lazy. For lazy evaluation, use generators

## GENERATORS
# Just like xxx Comprehension, except LAZY
gen = (x ** 2 for x in range(100))

## NESTING XXX COMPREHENSIONS

# Same as the below block of code
def _make_gen():
	for x in range(100):
		yield x ** 2
gen = _make_gen()

## ASSERTIONS
assert hasattr(l, "__iter__")
assert type(l) is list, 'Strange Type'
# `rank_test`: Test cell
print("{}. {}: {}".format(l, d, "This is print"))
# IS does not check value, so you cannot use: tup is ((1,2), (20, 30))
assert type(tup) is tuple and tup == ((1,2), (20, 30))


# REDUCE Function 
import functools
functools.reduce(lambda x, y: print(x), [1, 2, 3, 4, 5])
#1
#None
#None
#None

functools.reduce(lambda x, y: print(y), [1, 2, 3, 4, 5])
#2
#3
#4
#5

# When you want to run the function on all values of the input
functools.reduce(lambda x, y: print(y), [1, 2, 3, 4, 5], 0)
#1
#2
#3
#4
#5

functools.reduce(lambda x, y: print(x), [1, 2, 3, 4, 5], 0)
# 0
# None
# None
# None
# None

# eg:
points = [20, 10, 5, 0]
ranks = [0, 1, 2]
x = functools.reduce(lambda accum, x: accum + points[x], ranks, 0)








    
