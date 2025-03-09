# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89

# output- B
# A: 90-100

# B: 80-89

# C: 70-79

# D: 60-69

# F: 0-59

# If, elif, else

Score = int(input("Enter the score of the student: \n"))

if Score >= 90 and Score <= 100:
    print("Grade of the student is A")
elif Score >= 80 and Score <= 89:
    print("Grade of the student is B")
elif Score >= 70  and Score <= 79:
    print("grade of the student is C")
elif Score >= 60 and Score <= 69:
    print("grade of the student is D")
else:
    print("grade of the student is f")
