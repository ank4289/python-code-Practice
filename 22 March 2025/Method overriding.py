# Method Overriding - Same name in the parent and child
# child always overide the parent functions
# super means call my parent function


class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bow bow")


animalsound=Animal()
animalsound.sound()

animalsound=Dog()
animalsound.sound()