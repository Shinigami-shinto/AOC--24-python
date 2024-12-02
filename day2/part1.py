from typing import List, Tuple
from time import time

# Constants
START = time()
SAFE_COUNTER = 0

# Functions
def check_deltas_constraint(deltas: List) -> bool:
    for i in deltas:
        if i in [1,2,3]:
            continue
        else: return False
    return True
    
def check_continuity(row: List) -> Tuple[bool, List]:
    continuity = ''
    increase_check = '+' * (len(row)-1)
    decrease_check = '-' * (len(row)-1)
    deltas = []
    try:
        for i in range(len(row) - 1):
            deltas.append(abs(row[i]-row[i+1]))
            if row[i] > row[i+1]:
                # Decreasing
                continuity += '-'
                
            elif row[i] < row[i+1]:
                # Increasing sequence?
                continuity += '+'        
            else: return (False, [])
    except IndexError:
        print(f"index out of range for row {row}")
        
    if continuity == increase_check or continuity == decrease_check:
        return (True, deltas)
    else: return(False, [])

# 'Main' function starts here
# Read the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

input_list = []

# Process the lines into a list
for line in lines:
    row = list(map(int, line.split()))
    input_list.append(row)

for row in input_list:
    # Write function to process a row
    result, deltas = check_continuity(row)
    if result:
        # Write function to verify delta constraints
        if check_deltas_constraint(deltas): SAFE_COUNTER += 1

print(f"Safe counter: {SAFE_COUNTER}")        
        
END = time()
print(f"\n\nProgram took {END-START} time to execute")