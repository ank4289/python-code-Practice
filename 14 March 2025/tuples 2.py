tuple3 = tuple(["Pramod", "Lucky"])
print(tuple3)
print(tuple3[0])
print(tuple3[1])

# Merging Tuples
a=tuple(["Raghav is my"])
b= tuple(["HEro"])
c=a+b
print(c)

# Convert to List
my_tuple = (1, 2, 3, 4, 5)
print(list(my_tuple))

a,b=4,5
c,d,e = (9,10,11)
print(c)
print(d)
print(e)

# Nested Tuples

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team=(hero1,hero2)
print(awesome_team)
print(awesome_team[0])
print(awesome_team[1])

print(awesome_team[0][1])
print(awesome_team[1][1])

# Search in Tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Tokyo"in cities)
print("Aus" in cities)