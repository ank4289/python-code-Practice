list=[1,2,3,4,5,6]

small=min(list)
print(small)

small=list[0]

for i in list:
    if i < small:
        small = i

print("smallest number in the list :",small)