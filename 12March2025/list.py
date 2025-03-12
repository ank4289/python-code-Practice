# List - Collection of Items( Duplicate is allowed)
my_list=[1,2,3]
my_list2 = [1, True, "Pramod", 12.34]

print("my list",my_list)

# Indexing
print("Element at index 0:", my_list[0])
# Changing an element
my_list[1]=20
print(my_list)

#append()
my_list.append(5)
print("List after appending:", my_list)

#extend()
my_list.extend([5,6])
print("List after extending:", my_list)

#insert
my_list.insert(1,"a")
print("List after inserting 'a' at index 1:", my_list)

#remove
my_list.remove("a")
print("List after removing 'a':", my_list)

#clear and copy
my_list_copy=my_list.copy()
print(my_list_copy)

my_list.clear()
print("Initial list:", my_list)

print(my_list_copy)

my_list_copy.sort()
print(my_list_copy)
my_list_copy.reverse()
print(my_list_copy)

print(my_list_copy[0])
print(my_list_copy[1])
print(my_list_copy[2])
print(my_list_copy[3])

print(len(my_list_copy))

my_list=my_list_copy.copy()
print(my_list.remove(3))
print(my_list)