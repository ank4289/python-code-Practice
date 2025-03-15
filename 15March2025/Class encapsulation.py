# Encapsulation
# Data Members(Attributes) and Methods Together in a class
# Person -> name,age and eat(), sleep()


# Visibility

# !! Public Member
# Public members have no special naming convention in Python and
# are accessible from anywhere.
# They can be accessed directly from outside the class and other modules.


# ----------------------
# !! Protected Member
# Protected members are denoted by a single underscore prefix (_).
# They can still be accessed from outside the class, but it is considered a
# best practice not to do so directly.

# ----------------------
# !! Private  Member
# Private members are denoted by a double underscore prefix (__).
# Private members are intended to be used within the class only.

class myclass:
    def __init__(self):
        self.public_var=10
        self._protected_var=12
        self.__private_var=15

    def public_method(self):
        print("this is public method")
    def protectedmethod(self):
        print("this is protected method")
        print(self.__private_var)

    def privatemethod(self):
        print("this is private method")
        print(self._protected_var)

obj=myclass()
obj.public_method()
obj.protectedmethod()
obj.privatemethod()