#Count vowels and consonants in a String

name=input("Enter your name \n")
vowel="aeiouAEIOU"
sum=0
consonent=0

for char in name:
    if char in vowel:
        sum=sum+1
    else:
        consonent=consonent+1

print("Number of vowels:", sum)
print("Number of consonants:", consonent)






