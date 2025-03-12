# Map and Filter in the List


# Map Functions ( where we will go from one item and apply a functions)
numbers = [1, 2, 3, 4, 5]
# sq_numbers = [1, 4, 9, 16, 25]

sq=lambda x:x*x
sq_number=[]
for i in numbers:
    sq_number.append(sq(i))

print(sq_number)

def ThreeTimes(a):
    return a ** 3

sq_number3=list(map(lambda x:x*x,numbers))
print(sq_number3)
sq_number4=list(map(ThreeTimes,numbers))
print(sq_number4)
