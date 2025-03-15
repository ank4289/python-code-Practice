numbers = [1, -2, -3, -4, 5, 16, -7, 8, -9, -10]

def positivenum(num):
    return num > 0


postive=filter(positivenum,numbers)
print(postive)
positive_list=list(postive)
print(positive_list)
