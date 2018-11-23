# Demo class to illustrate the syntax of a python class
# Illustrates inheritance, getters/setters, private and public properties


class MyParent1:
  def __init__(self):
    print ("Hello from " + str(self.__class__.__name__))

  
class MyParent2:
  pass


# Inheriting from object is necessary for @property etc to work OK
# This is called "new style" classes
class MyClass(object, MyParent1, MyParent2):        # Multiple inheritance is OK

  "======== My Doc String ==========="   
  
  def __init__(self, param1=None):                  # __init__ is like a constructor, it is called after creating an object. By convention it's the first method of a class

      MyParent1.__init__(self)                      # Initialize our parent(s), MUST be done explicitly
      
      self.__private_prop1 = "I'm Private"          # Declare and initialize our object (private) properties
      self.public_prop1 = "I'm Public"              # Declare and initialize our object (public) properties
      self.__public_prop2__ = "I'm also Public"     # Declare and initialize our object (public) properties
      ## self["name"] = param1                      # To use this syntax you need to define the __setitem__() function

  # Property1 is exposed using getters and setters. Similarly a "deleter" can also be declared using @prop_name.deleter
  @property
  def public_prop1(self):
    print("Getting value")
    return self.__public_prop1

  @public_prop1.setter
  def public_prop1(self, value):
    print("Setting value")
    self.__public_prop1 = value + "++setter++"
    
  # Destructor
  def __del__(self):
    print("Don't delete me!")
    
  # Context manager used along with the WITH keyword
  # https://docs.python.org/2/reference/compound_stmts.html#with
  # https://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python/
  



if __name__ == "__main__":
  o1 = MyClass("Govind")
  o2 = MyParent1()

  print(o1.public_prop1)
  ## print(o1.__private_prop1) --> Won't run
  print(o1._MyClass__private_prop1) # However this works
  # More about introspection -> https://docs.python.org/3/library/inspect.html
  print(o1.__dict__) # because the interpreter mangles names prefixed with __name to _class__name
  print(o1.__public_prop2__)

  # Equivalence of Objects
  ox = o1
  if ox is o1:
    print("ox and o1 point to the same memory location = " + str(id(ox)))

