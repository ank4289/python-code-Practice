# Take a input from user we will create How

class car():
    color=None
    model=None

    def cardetails(self):
        print("your car details is ",self.color,self.model)

car_color=input("Please enter colore of the car \n")
car_model=input("please enter model of the car \n")

car_obj=car()
car_obj.color=car_color
car_obj.model=car_model
# Obj ref we can call the function
car_obj.cardetails()


# car_details()
