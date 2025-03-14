#Write a Python program to count the number of strings in a list
# where the string length is 2 or more and the first and last character are the same.

list=["NAMAN"]

count=0
for words in list:
    if len(words) >=2 and words[0] == words[-1]:
        count=+1

print("Count of matching strings:", count)


