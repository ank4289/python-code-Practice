# Abstraction - OOPs
# Hiding the details and showing the what is required

# Car ->  start the engine ->  put the gear -> start driving
# -> Do you know How engine is started? , How gear box was managed?
# hide the implementation and show only the important details


# to represent complex systems by simplifying and hiding unnecessary details

# ABC -> ? Abstract Base Class
# Abstract base Methods

# Shape -> Rectangle, Circle
# Shape -> perimeter, area

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class tiger:
    def sound(self):
        return "roar"


class pow:
    def sound(self):
        return "pow -pow"


tiger=tiger()
print(tiger.sound())

powpow=pow()
print(powpow.sound())
