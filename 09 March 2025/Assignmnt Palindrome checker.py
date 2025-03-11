

def reverse (input):
    revese_str=""
    for x in input:
        revese_str=x+revese_str
    return revese_str

inputstr="Ankit"
revesestrcall = reverse(inputstr)
print(revesestrcall)
if revesestrcall == inputstr:
    print("Pallindrome")
else:
    print("it is not")