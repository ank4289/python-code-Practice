fact=int(input("enter the number for factorial \n"))
num=1
for x in range(1,fact+1):
    num=num*x

print(f"Factorial of number {fact}:",num)
