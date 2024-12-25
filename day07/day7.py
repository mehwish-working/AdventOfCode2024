from itertools import product

def evaluate_expression(numbers, operators):
    """
    Evaluate an expression using left-to-right evaluation with the given operators.
    """
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_valid_equation(target, numbers, operators_set):
    """
    Check if the target can be reached using the provided operators (+, *, ||).
    """
    n = len(numbers) - 1
    for ops in product(operators_set, repeat=n):
        if evaluate_expression(numbers, ops) == target:
            return True
    return False

def calculate_calibration_results(file_name, operators_set):
    """
    Read the input file, process each equation, and calculate the total calibration result.
    """
    total_calibration = 0

    with open(file_name, 'r') as file:
        for line in file:
            target, nums = line.strip().split(':')
            target = int(target)
            numbers = list(map(int, nums.split()))

            if is_valid_equation(target, numbers, operators_set):
                total_calibration += target

    return total_calibration

if __name__ == "__main__":
    # Input file name
    input_file = "input.txt"
    
    # Part 1: Using only + and *
    operators_part1 = ['+', '*']
    result_part1 = calculate_calibration_results(input_file, operators_part1)
    print("Part 1 - Total Calibration Result:", result_part1)
    
    # Part 2: Using +, *, and ||
    operators_part2 = ['+', '*', '||']
    result_part2 = calculate_calibration_results(input_file, operators_part2)
    print("Part 2 - Total Calibration Result:", result_part2)
