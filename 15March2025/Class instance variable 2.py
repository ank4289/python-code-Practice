class Person:
    def __init__(self):
        print("instance variable has started")


    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("you started it")

    def details(self):
        print("your details are as ",self.name,self.age)

    def details2(self):
        print("your details are as ", self.name*2)


ankit=Person("amit",34)
ankit.details()

ram=Person("ram",45)
ram.details()
