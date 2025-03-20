# Parent - Child
# Father -> son
# GF -> F -> S
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:
    def car(self):
        print("lambo")

    def speak(self):
        print("Animal speak")

class Dog(Animal):
    pass

dog=Dog()
dog.speak()