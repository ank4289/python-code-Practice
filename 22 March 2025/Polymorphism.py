# Poly
# ABC
# Exception

# Polymorphism - object-oriented programming (OOP)
# object -> behave differently based on the sti.
# Person -> Amit, Pramod -> talk() , Amit can talk in hindi, pramod can talk in english


class Shape:
    def area(self):
        print("shape of the class")

class Recatangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius


shape1=Recatangle(2,3)
print(shape1.area())

shape2=Circle(10)
print(shape2.area())

shape3=Shape()
shape3.area()