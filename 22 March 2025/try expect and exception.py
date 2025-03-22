#try:
    #file=open("two2",'r')
    #file.read()
    #file.close()
#except FileNotFoundError as file:
    #print(file)

#Read
try:
    file=open("Ankit",'r')
    file.read()
except FileExistsError as exist:
    if file:
        file.close()