# Part 01

import re
def sum_of_multiplications(file_path):
    # Read the corrupted memory from the file
    with open(file_path, 'r') as file:
        corrupted_memory = file.read()

    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all valid matches
    matches = re.findall(pattern, corrupted_memory)

    # Calculate the sum of all multiplications
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum


# File path to input.txt
file_path = "input.txt"

# Get the result
result = sum_of_multiplications(file_path)

# Output the result
print("Sum of all valid multiplications:", result)

# ----------------------------------------------
# Part 02

import re

# Read input from input.txt
with open('input.txt', 'r') as file:
    data = file.read()

# Initialize state and result
is_mul_enabled = True  # mul is enabled initially
total_sum = 0

# Regular expression to match instructions
pattern = re.compile(r'do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)')

# Process each instruction
for match in pattern.finditer(data):
    instruction = match.group(0)  # The full matched instruction
    if instruction == "do()":
        is_mul_enabled = True
    elif instruction == "don't()":
        is_mul_enabled = False
    else:  # It's a mul instruction
        # Extract numbers for mul(a, b)
        a, b = map(int, match.groups())
        if is_mul_enabled:
            total_sum += a * b

# Output the total sum
print(f"Total sum of enabled multiplications: {total_sum}")

