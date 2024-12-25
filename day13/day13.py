# Part 01
def read_input(filename):
    machines = []
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n\n')
    for group in data:
        a_str, b_str, p_str = group.strip().split('\n')

        ax, ay = [int(x[2:]) for x in a_str[10:].split(', ')]
        bx, by = [int(x[2:]) for x in b_str[10:].split(', ')]
        px, py = [int(x[2:]) for x in p_str[7:].split(', ')]

        machines.append({
            'xA': ax, 'yA': ay,
            'xB': bx, 'yB': by,
            'xP': px, 'yP': py
        })
    return machines

def find_min_cost_part1(machine):
    max_presses = 100
    min_cost = None
    for nA in range(max_presses + 1):
        for nB in range(max_presses + 1):
            x_total = nA * machine['xA'] + nB * machine['xB']
            y_total = nA * machine['yA'] + nB * machine['yB']
            if x_total == machine['xP'] and y_total == machine['yP']:
                cost = nA * 3 + nB * 1
                if min_cost is None or cost < min_cost:
                    min_cost = cost
    return min_cost

def find_min_cost_part2(machines):
    total = 0
    offset = 10000000000000
    for machine in machines:
        ax, ay = machine['xA'], machine['yA']
        bx, by = machine['xB'], machine['yB']
        px, py = machine['xP'] + offset, machine['yP'] + offset

        denominator = ax * by - ay * bx
        numerator_m = px * by - py * bx

        if denominator == 0 or numerator_m % denominator != 0:
            continue

        m = numerator_m // denominator
        if m < 0:
            continue

        numerator_n = py - ay * m
        if by == 0 or numerator_n % by != 0:
            continue

        n = numerator_n // by
        if n < 0:
            continue

        total += 3 * m + n
    return total

def main():
    filename = 'input.txt'
    machines = read_input(filename)

    # Part One
    total_cost_part1 = 0
    for machine in machines:
        cost = find_min_cost_part1(machine)
        if cost is not None:
            total_cost_part1 += cost

    print("Part One - Minimum tokens to win all possible prizes:", total_cost_part1)

    # Part Two
    total_cost_part2 = find_min_cost_part2(machines)
    print("Part Two - Minimum tokens to win all possible prizes:", total_cost_part2)

if __name__ == "__main__":
    main()