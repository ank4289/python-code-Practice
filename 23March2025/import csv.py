import csv

with open("C:/Users/Acer/Desktop/Python class Testing academy Pramod/testdata.csv",newline='') as file:
    reader=csv.reader(file)
    for row in reader:
        print('|'.join(row))
