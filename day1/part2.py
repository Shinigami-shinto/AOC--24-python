from typing import List
import os, sys
print(os.getcwd())
print(sys.platform)
# Read the input file
with open("input-part1.txt", "r") as file:
    lines = file.readlines()

# Initialize two separate arrays
array1 = []
array2 = []

# Process the lines into two separate arrays
for line in lines:
    num1, num2 = map(int, line.split())
    array1.append(num1)
    array2.append(num2)

# Now you have two separate arrays
print("Array 1:", array1[:10])
print("Array 2:", array2[:10])

similarity = 0
for i in array1:
    match_count = 0
    for j in array2:
        if i == j:
            match_count += 1
    similarity += (i * match_count)

print(f"similarity score: {similarity}")