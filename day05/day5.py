# Part 01

# Step 1: Read the input file and parse the data
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Separate rules and updates
    rules = []
    updates = []
    is_rule = True
    
    for line in lines:
        if line == "":
            is_rule = False  # Switch to updates
        elif is_rule:
            rules.append(line.strip())
        else:
            updates.append(line.strip())
    
    return rules, updates

# Step 2: Parse rules into a dictionary
def parse_rules(rules):
    rule_dict = {}
    for rule in rules:
        x, y = map(int, rule.split("|"))
        if x not in rule_dict:
            rule_dict[x] = []
        rule_dict[x].append(y)
    return rule_dict

# Step 3: Check if an update is in the correct order
def is_update_valid(update, rule_dict):
    pages = list(map(int, update.split(",")))
    page_index = {page: i for i, page in enumerate(pages)}  # Page to index mapping

    # Validate each rule
    for x, ys in rule_dict.items():
        if x in page_index:
            for y in ys:
                if y in page_index and page_index[x] > page_index[y]:  # Rule violation
                    return False
    return True

# Step 4: Find the middle page number of a list
def find_middle_page(pages):
    n = len(pages)
    return pages[n // 2]  # Middle element (0-based indexing)

# Step 5: Process all updates and calculate the sum
def calculate_sum_of_middle_pages(rules, updates):
    rule_dict = parse_rules(rules)
    total_sum = 0

    for update in updates:
        if is_update_valid(update, rule_dict):
            pages = list(map(int, update.split(",")))
            total_sum += find_middle_page(pages)
    
    return total_sum

# Main function to execute the solution
def main():
    # Read input from input.txt
    rules, updates = read_input("input.txt")
    
    # Calculate the sum of middle pages of correctly ordered updates
    result = calculate_sum_of_middle_pages(rules, updates)
    
    print("Sum of middle pages:", result)

if __name__ == "__main__":
    main()

# -------------------------------------
# Part 02
# Step 1: Read the input file and parse the data
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().strip().split("\n")
    
    # Separate rules and updates
    rules = []
    updates = []
    is_rule = True
    
    for line in lines:
        if line == "":
            is_rule = False  # Switch to updates
        elif is_rule:
            rules.append(line.strip())
        else:
            updates.append(line.strip())
    
    return rules, updates

# Step 2: Parse rules into a dictionary
def parse_rules(rules):
    rule_dict = {}
    for rule in rules:
        x, y = map(int, rule.split("|"))
        if x not in rule_dict:
            rule_dict[x] = []
        rule_dict[x].append(y)
    return rule_dict

# Step 3: Check if an update is in the correct order
def is_update_valid(update, rule_dict):
    pages = list(map(int, update.split(",")))
    page_index = {page: i for i, page in enumerate(pages)}  # Page to index mapping

    # Validate each rule
    for x, ys in rule_dict.items():
        if x in page_index:
            for y in ys:
                if y in page_index and page_index[x] > page_index[y]:  # Rule violation
                    return False
    return True

# Step 4: Correct the order of an update
def correct_order(update, rule_dict):
    pages = list(map(int, update.split(",")))
    
    # Use Topological Sorting to arrange pages based on rules
    from collections import defaultdict, deque

    # Build graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for x in pages:
        in_degree[x] = 0  # Initialize in-degrees for all pages
    
    for x in pages:
        if x in rule_dict:
            for y in rule_dict[x]:
                if y in pages:  # Only consider rules within the current update
                    graph[x].append(y)
                    in_degree[y] += 1

    # Topological Sort
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

# Step 5: Find the middle page number of a list
def find_middle_page(pages):
    n = len(pages)
    return pages[n // 2]  # Middle element (0-based indexing)

# Step 6: Process incorrect updates and calculate the sum
def calculate_sum_of_corrected_middle_pages(rules, updates):
    rule_dict = parse_rules(rules)
    total_sum = 0

    for update in updates:
        if not is_update_valid(update, rule_dict):  # Incorrect updates
            corrected = correct_order(update, rule_dict)
            total_sum += find_middle_page(corrected)
    
    return total_sum

# Main function to execute the solution
def main():
    # Read input from input.txt
    rules, updates = read_input("input.txt")
    
    # Calculate the sum of middle pages of corrected updates
    result = calculate_sum_of_corrected_middle_pages(rules, updates)
    
    print("Sum of middle pages after correction:", result)

if __name__ == "__main__":
    main()
