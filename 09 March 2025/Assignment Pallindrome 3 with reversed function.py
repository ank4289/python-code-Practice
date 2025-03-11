

def reverse(a):
    return "".join(reversed(a))

input = "Ankit"
reverse_str= reverse(input)
print(reverse_str)
if input == reverse_str:
    print("it is a pallindrome")
else:
    print("it is not")