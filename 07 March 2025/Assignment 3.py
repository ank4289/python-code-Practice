#Explain the difference between the = operator and the == operator in Python
#Answer:
# In Python, the operators = and == serve very different purposes,
#  don’t have much relation at all other than similar syntax.
#The = operator is used for assignment, such as when assigning a value to a variable.
#The == operator is the relational operator for checking equality of two values.
# If the values are the same, it will return True, and will return False otherwise.
import math

#2.What does the ** operator do in Python, and how is it used?
#it raise to the power of n if n**=2 and n is number passed then it will
#translate to if n=2 then n**2 will be (2 raise to power 2) which is 4
n=2
square=n**2
print(square)

#3What does the ^ operator do in Python, and in what context is it commonly used?
#The ^ operator in Python is the bitwise XOR (exclusive OR) operator. It performs a bitwise XOR operation between corresponding bits of two integers.

#How XOR Works:
#The result is 1 if the corresponding bits of the operands are different.
#The result is 0 if the corresponding bits of the operands are the same.
#Example:
a = 5  # 0b0101
b = 3  # 0b0011
result = a ^ b  # 0b0110 (which is 6 in decimal)
print(result)  # Output: 6

#4Write a Python program to calculate the area of a circle given its radius using the formula
#area=π×r^2 ( Take pie as 3.14)

radius=float(input("enter the radius of circle\n"))
print("radius is ",radius)
r=radius**2
print("Square root of radius is ",r)
Area=math.pi*r
print("Area of circle is",Area)

#5Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.

A=int(input("Enter first number \n"))
b=int(input("Enter second number \n"))
compare= A if A >= b else b
print(f"Between {A}  and {b} greater number is ",compare)

#Use the ternary operator to find the maximum of three numbers entered by the user.
num1=int(input("Enter first number \n"))
num2=int(input("Enter second number \n"))
num3=int(input("Enter third number \n"))
Maxval= num1 if num1>=num2 else num2
maxval2= Maxval if Maxval>=num3 else num3
print("maximum number out of the 3 is ",maxval2)

#Develop a Python script that calculates the square and cube of a given number.

Number=int(input("Please enter the number for square and cube calculation \n"))
Number**=2
print("Square root of the number is ",Number)
Number2=int(input("Please enter the number for square and cube calculation \n"))
Number2**=3
print("cube root of the number is ",Number2)



