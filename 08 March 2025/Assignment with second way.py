#Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.

A=int(input("Enter first number \n"))
b=int(input("Enter second number \n"))
compare= "Greater than" if A > b else "less than" if A < b else "equal to"
print(f"{A} is {compare} than {b}")
5