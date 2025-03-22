from collections import namedtuple
Per= namedtuple("Person",("name", "age", "gender"))
Person=Per("Ankit",35,"male")
print("Name",Person.name)
print("Age",Person.age)
print("gender",Person.gender)