my_dict = {'b': 2, 'a': 1, 'c': 3}

val=my_dict.pop('a')
print(val)

print(my_dict)
my_dict['a']=val
print(my_dict)

# OrderedDict
# key-value pairs based on the order of insertion

# list, set, tuple, dict, OrderedDict, - API Automation and Selenium

from collections import OrderedDict
od=OrderedDict()
od['a']=22
od['b']=33
od['c']=44
od['d']=55

print(od)
# Selenium - Insert the Web elements into a Dict
# You want to keep the order - login elemtns, dashboard elements,

# Dict - It will not keep the Order of insertion
# OrderedDict - It will keep the order of insertion
keys=list(od.keys())
print(keys)
key_sort=sorted(keys)
print(key_sort)

key_sort_rev=sorted(keys,reverse=True)
print(key_sort_rev)
