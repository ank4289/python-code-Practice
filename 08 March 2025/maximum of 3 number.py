# Find the maximum of three numbers using the ternary operator:

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

maxnumber= num1 if (num1 > num2 and num1 > num3) else (num2 if num2 >num3 else num3)

print(f"the max number of {num1},{num2} and {num3} is",maxnumber)