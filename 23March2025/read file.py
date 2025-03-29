try:
    with open("Ankit.txt",'r') as file:
        content=file.read()
        print(content)
except FileNotFoundError as error:
    print(error)

