t=("TheTestingAcademy","for","TheTestingAcademy")
print(t)
print("\nSet with the use of Tuple: ")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}

myset=set1.union(set2)
print(myset)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
myset2=set1.intersection(set2)
print(myset2)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
diff1=set1.difference(set2)
diff2=set2.difference(set1)

print(diff1)
print(diff2)


set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
subset=set2.issubset(set1)
print(subset)


set1=set(["TheTestingAcademy", "For", "TheTestingAcademy."])
print(set1)

for i in set1:
    print(i)

set1=set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])

set1.remove(5)
set1.remove(6)

print(set1)