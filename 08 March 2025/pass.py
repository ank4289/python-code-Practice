#Pass means to skip any loop or condition
for x in range (1,10):
    if x == 5:
        pass
    else:
        print(x)


#continue help to continue to next line of code

for x in range(1,10):
    if x%2==0:
        print("even number")
        continue
        print(x)
