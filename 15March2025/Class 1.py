# Class and Object in Python.

# Person(class)
# Attributes - name,age, phone_no, height, weight, gender, prof
# Methods - Can do -> Run(), sleep(). sing(), talk(), eat(), fight(), learn(), hear(), think()


# Objects
# Amit
# Durga - GENDER  - fEMALE
# Santosh -

class person:
    # Attributes
    name= None
    age= None
    phone_no= None
    height=None
    weight=None
    gender=None
    prof=None

    # Methods
    def talk(self):
        print("Talk")

    def sleep(self):
        print("sleep")

    def walk(self):
        return "i am walking"

amit_object=person()
amit_object.name="ankit"
amit_object.age=12
amit_object.gender="Male"
amit_object.prof="QA"
print(amit_object)
amit_object.sleep()
amit_object.talk()

durga_obj=person()
durga_obj.phone_no=123
durga_obj.sleep()


