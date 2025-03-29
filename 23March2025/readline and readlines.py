#with open("newtext","r") as file:
#    content=file.readline()
 ##   print(content)

with open("newtext","r") as file:
    lines=file.readlines()
    print(lines)
    for line in lines:
        print(line,end="")