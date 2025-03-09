#Create a program that determines whether a given year is a leap year.
#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#se an if-else statement to make this determination.
#Input = 2024
#Output = Leap year


YR=int(input("Enter the year :"))
print(YR)

if YR%4 == 0 or YR%400 == 0:
    print("Entered year is leap Year")
    print(YR%4)
    print(YR%400)
elif YR%100 != 0:
    print(YR%100)
    print("Not a leap year")


