numList = [30, 2, -15, 17, 9, 100]
list_of_number_greter_than_10 =list(filter(lambda x:x > 10, numList))
print(list_of_number_greter_than_10)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def even(num):
    return num%2==0

tuple_even=tuple(filter(even,numbers_tuple))
print(tuple_even)

l = [(1, 23), (34, 34)]
print(l)
print(l[0][0])
print(l[0][1])
print(l[1][0])
print(l[1][1])