class Myclass:
    def __init__(self):
        self.__private_toilet="Private Toilet Only Pramod Allowed"
        self.__protected_attribute= 42
        self.public_var= 55

    def private_method(self):
        return "this is a private method."



obj=Myclass()
print(obj.private_method())

