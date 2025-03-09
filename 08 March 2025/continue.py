#continue help to continue to next line of code

for x in range(1,10):
    if x%2==0:
        print(f"even number is: {x}")
        continue
    print(f"odd number is :{x}")