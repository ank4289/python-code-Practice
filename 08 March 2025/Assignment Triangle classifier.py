#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.
#3 Input side 1, side 2 and side 3
#output - Eq, Iso, Scalene -
#Eq. = side 1 == side 2 = side 3

S1=int(input("Enter first side: \n"))
S2=int(input("Enter second side: \n"))
S3=int(input("Enter third side: \n"))

if S1 == S2 != S3 or S3 == S2 != S1:
    print("the triangle is isosceles")
elif S1 == S2 and S1 == S3:
    print("The triangle is equilateral")
else:
    print("The Triangle is scalene")