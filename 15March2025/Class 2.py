# Car -
# Objects - Tesla, Lambo

class Car:
    name=None
    color=None
    model=None
    speed=None
    engine=None
# self is a special variable that is used within the context of
# object-oriented programming (OOP).
# It is a reference to the instance of a class
# access and manipulate the attributes and methods of that instance / Object

    def start_engine(self):
        print("starting engine")

    def drive(self):
        print("drive")
    def car_break(self):
        print("break")

    def who_is_drivinvg(self):
        print("I am driving"+self.name)


tesla_obj_ref_tesla = Car() # This is instance of a Class - Object
lambo_obj_ref_lambo = Car() # This is instance of a Class - Object

tesla_obj_ref_tesla.name="tesla"
lambo_obj_ref_lambo.name="lambo"

tesla_obj_ref_tesla.who_is_drivinvg()
lambo_obj_ref_lambo.who_is_drivinvg()