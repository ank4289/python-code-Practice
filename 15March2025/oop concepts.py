numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_num(num):
    return num%2==0

evennumber=filter(even_num,numbers)
print(evennumber)
evennumber_list= list(evennumber)
print(evennumber_list)