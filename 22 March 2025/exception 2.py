A=int(input("please enter first:"))
B=int(input("please enter second:"))
try:
    C=A/B
    print(C)
except Exception as error:
    print("the exception is :",error)