def can_create_design(design, patterns, memo):
    if design in memo:
        return memo[design]

    if not design:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if can_create_design(design[len(pattern):], patterns, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False


def count_possible_designs(input_file):
    with open(input_file, 'r') as file:
        lines = file.read().strip().split('\n')

    # Split patterns and designs
    patterns = lines[0].split(', ')
    designs = lines[2:]  # Skip the blank line

    # Count how many designs are possible
    memo = {}
    count = sum(can_create_design(design, patterns, memo) for design in designs)
    return count


if __name__ == "__main__":
    input_file = "input.txt"
    result = count_possible_designs(input_file)
    print(f"Number of possible designs: {result}")

# --------------------------------------------------------------------------
from collections import defaultdict

def count_ways_to_form_design(patterns, design, memo):
    if design in memo:
        return memo[design]

    if not design:
        return 1  # Base case: one way to form an empty design

    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            remaining_design = design[len(pattern):]
            total_ways += count_ways_to_form_design(patterns, remaining_design, memo)

    memo[design] = total_ways
    return total_ways

def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    # Parse input
    patterns = lines[0].split(", ")
    designs = lines[2:]  # Skip the blank line

    total_combinations = 0
    for design in designs:
        memo = {}
        total_combinations += count_ways_to_form_design(patterns, design, memo)

    print("Total number of ways to form all designs:", total_combinations)

if __name__ == "__main__":
    main()
