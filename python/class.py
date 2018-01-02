# Demo class to illustrate the syntax of a python class
# Illustrates inheritance, getters/setters, private and public properties


class MyParent1:
  def __init__(self):
    print ("Hello from " + str(self.__class__.__name__))

  
class MyParent2:
  pass


# Inheriting from object is necessary for @property etc to work OK
# This is called "new style" classes
class MyClass(object, MyParent1, MyParent2):

  "======== My Doc String ==========="   
  
  def __init__(self, param1=None):

      MyParent1.__init__(self)                 # Initialize our parent(s), MUST be done explicitly
      
      self.__private_prop1 = "I'm Private"     # Declare and initialize our object (private) properties
      self.public_prop1 = "I'm Public"         # Declare and initialize our object (public) properties
      self.__public_prop2__ = "I'm also Public"         # Declare and initialize our object (public) properties
      ## self["name"] = param1                 # To use this syntax you need to define the __setitem__() function

  # Property1 is exposed using getters and setters. Similarly a "deleter" can also be declared using @prop_name.deleter
  @property
  def public_prop1(self):
    print("Getting value")
    return self.__public_prop1

  @public_prop1.setter
  def public_prop1(self, value):
    print("Setting value")
    self.__public_prop1 = value + "++setter++"



if __name__ == "__main__":
  o1 = MyClass("Govind")
  o2 = MyParent1()

  print(o1.public_prop1)
  ## print(o1.__private_prop1) --> Won't run
  print(o1.__public_prop2__)
