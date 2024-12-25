#Part 01
def calculate_total_distance(file_path):
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []

        # Read and parse data
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Sort the lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

    return total_distance


# File path to input.txt
file_path = 'input.txt'

# Compute and print the result
result = calculate_total_distance(file_path)
print("Total Distance:", result)

# ---------------------------------------------------

# Part 02
from collections import Counter
def calculate_similarity_score(file_path):# PART
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []

        # Read and parse data
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Count frequencies in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(left * right_count[left] for left in left_list)

    return similarity_score

# File path to input1.txt
file_path = 'input.txt'

# Compute and print the result
result = calculate_similarity_score(file_path)
print("Similarity Score:", result)

