import csv

with open('testfile.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        for value in row:
            print(value,end='-')
            print()

#with statement is used it automatically closes the file that opned