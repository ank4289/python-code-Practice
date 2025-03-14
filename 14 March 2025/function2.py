num=20

def multiplyby10(n):
    n*=10
    num=n # Changing the value inside the function'
    print("Value of num inside function:", num)
    return n

op=multiplyby10(num)
print(op)
print("Value of num outside function:", num)