my_dict = {'a': 1, 'b': 2}

remove=my_dict.pop('a')
print(remove)
print(my_dict)
# API Testing -> JSON so we can use Dict which is similar data type as JSON
print(dir(my_dict))

# How to Iterate over the Dict?
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

item=knights.items()
length=len(knights)
print(length)
print(item)
for i,v in item:
    print(i,v)