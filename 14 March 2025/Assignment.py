numbers = [1,2,3,4,5,6]
largest = max(numbers)
print(largest)  # Output: 9


numbers = [3, 7, 2, 9, 5]
largest = numbers[0]  # Assume first number is the largest

for num in numbers:
    if num > largest:
        largest = num

print(largest)  # Output: 9



