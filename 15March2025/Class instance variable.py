class car:
    name="pramod"
    def __init__(self,make,model):
        self.make =make
        self.model=model
        print("i will be called first")

    def startengine(self):
        print("start the engine of ",self.make,self.model)


car1=car("Toyota","AE-86")
car2=car("honda","CIVIC TYPE R")

car1.startengine()
#car2.startengine()

print(id(car1))
print(id(car2))

# Object is created a Special Function is called automatically __int__()
# All the attribute Object you can initilize - add some initial value to them

#default constructor
