# Method Overloading:
# Python does not support method overloading in the traditional sense
# Same name of a function with different Parameter
#Onlt Method overiding is supported
#if we pass defaut value then we can call that function or object


class Mathuitil:
    def Add(self,a,b):
        print(a+b)

    def Add(self,a,b=0,c=0):
        return a+b+c


Math1=Mathuitil()
Add1=Math1.Add(2,3)
print(Add1)
Add2=Math1.Add(3,4,7)
print(Add2)

Add3=Math1.Add(2)
print(Add3)

