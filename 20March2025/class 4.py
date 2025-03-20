# Multilevel Inheritance
#Level - GF -> F -> S

class grandfather:
    def grandfather_method(self):
        return "grandparents method"


class Parent(grandfather):
    def parent_method(self):
        return "Parent is method"


class child(Parent):
    def child_method(self):
        return "child method"


chil =child()
print(chil.grandfather_method())
print(chil.parent_method())
print(chil.child_method())