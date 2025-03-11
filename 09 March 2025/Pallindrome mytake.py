#Task: Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121'
def Palindrome():
    Name = input("Please enter a name \n")
    Rev = Name[::-1]  # Reverse the whole string
    print(Rev)
    if Name == Rev:
        print("This string is Palindrom")
    else:
        print("Not a Palindrome")


Palindrome()
