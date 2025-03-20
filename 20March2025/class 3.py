
# Single Inheritance - 90%
# Use the properties, variables and methods of your base class or parent class by the sub class or son class

class father:
    bank_bal=100


    def one_bhk(self):
        print("use it please")


class son(father):
    pass

so=son()
so.one_bhk()
