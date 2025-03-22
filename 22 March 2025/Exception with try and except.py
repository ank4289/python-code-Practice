# Exception
# An exception is an event that occurs during the execution of a program
# that disrupts the normal flow of instructions.
a=10
b=0
try:
    c=a/b
#except ZeroDivisionError as error:
    #print("it cannot be done because",error)

except Exception as error2:
    print("it cannot be done becuase",error2)