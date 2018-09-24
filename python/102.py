
## MAGIC variables

### 1. *args and **kwargs for variable length arguments for functions

# *args allows you to recieve "non-keyed" variable argument list
# **kwargs allows for "key worded" data in the variable argument list
# The key "magic" element is the asterix, the "args" is not mandatory
def func(normal_arg, *args):
    print("Normal Arg = " + str(normal_arg))
    print("Variable arg list = {}".format(args))

def funckw(normal_arg, **kwargs):
    print("Normal Arg = " + str(normal_arg))
    print("Variable arg list = {}".format(kwargs))
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


func("Norm", "Govind", 1, 2, 3)
funckw("Norm", name="Govind", place="India", suburb="Unknown")

# Even if functions are not defined with the varargs magic syntax, you can call them using *args and **kwargs
def normal_func(a1, a2, a3):
    print("{0} {1} {2}".format(a1, a2, a3))

arg = ["hi", "hello", "hoo"]    # The length of th parameter list should match the arg list
kwarg = {"a1":"hi", "a2":"hmm", "a3":"goo"} # the "key" should match the parameter name, and all params must be defined
normal_func(*arg)
normal_func(**kwarg)


### 2. Decorators
