# Hybrid Inheritance

# multiple types of inheritance, such as single, multiple, and multilevel inheritance.

class a:
    def a(self):
        return "method a"

class B(a):
    def b(self):
        return "method b"

class C(a):
    def c(self):
        return "method c"

class D(B,C):
    def d(self):
        return "method d"


d=D()
print(d.a())
print(d.b())
print(d.c())
print(d.d())
