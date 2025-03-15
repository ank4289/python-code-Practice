products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]

print(type(products))
print(type(products[0]))
print(products[0])

def is_affordableprice(ankit):
    return ankit["price"] <500

def is_affordable_name(ankit):
    return len(ankit["name"]) > 6

affordable_price=list(filter(is_affordableprice,products))
affordable_name=list(filter(is_affordable_name,products))

print(affordable_name)
print(affordable_price)

for i in affordable_price:
    print(i["price"],i["name"])

for i in affordable_name:
    print(i["price"],i["name"])


i=10
name="ankit"
print(i)
print(name)
print(name+str(i))
#print(int(name)+i)
