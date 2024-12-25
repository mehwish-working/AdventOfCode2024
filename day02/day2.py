def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    # Check if all differences are positive (increasing)
    if all(d > 0 for d in differences):
        if all(1 <= d <= 3 for d in differences):
            return True
    # Check if all differences are negative (decreasing)
    elif all(d < 0 for d in differences):
        if all(-3 <= d <= -1 for d in differences):
            return True
    return False

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

# Part 1: Count safe reports without the Problem Dampener
safe_reports_part1 = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.strip().split()]
        if is_safe(report):
            safe_reports_part1 += 1

print("Part 1 - Number of safe reports:", safe_reports_part1)

# -------------------------------------------------------------------
# Part 2: Count safe reports with the Problem Dampener

safe_reports_part2 = 0

with open('input.txt', 'r') as file:
    for line in file:
        report = [int(x) for x in line.strip().split()]
        if is_safe_with_dampener(report):
            safe_reports_part2 += 1

print("Part 2 - Number of safe reports with the Problem Dampener:", safe_reports_part2)