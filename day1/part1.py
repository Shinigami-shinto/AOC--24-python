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

# Sort the arrays
array1.sort()
array2.sort()

print("Sorted Array 1:", array1[:10])
print("Sorted Array 2:", array2[:10])

def distanceBetweenSortedLists(l1: List, l2: List) -> List :
    distances = []
    for i in range(len(l1)):
        distances.append(abs(l1[i]-l2[i]))
    return distances

solution = []
solution = sum(distanceBetweenSortedLists(array1, array2))

print(f"Solution: {solution}")

# # Write the solution to a file
# output_file = "solution-day1-part-1.txt"
# with open(output_file, "w") as file:
#     for line in solution:
#         file.write(line + "\n")