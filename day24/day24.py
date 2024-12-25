import os
from copy import deepcopy

def puzzle_input(filename):
    """Parsed input"""
    with open(filename, "r", encoding="utf-8") as inputdata:
        return parse_lines(inputdata.readlines())

def parse_lines(lines):
    result = {
        'wires': {},
        'gates': {}
    }
    parse_gates = False
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            parse_gates = True
            continue
        if parse_gates:
            gate, wire = line.split(' -> ')
            gate_parts = gate.split(' ')
            result['gates'][wire] = (gate_parts[1], (gate_parts[0], gate_parts[2]))
        else:
            wire, value = line.split(': ')
            result['wires'][wire] = int(value)

    return result

def get_decimal(data):
    local_data = deepcopy(data)

    binary = []
    pos = 0
    key = 'z' + str(pos).rjust(2, '0')
    while key in local_data['gates']:
        binary.append(get_value(local_data, key))
        pos += 1
        key = 'z' + str(pos).rjust(2, '0')

    result = 0
    for pos, val in enumerate(binary):
        result += val * (2 ** pos)

    return result

def get_value(data, key):
    if key not in data['wires']:
        if data['gates'][key][0] == 'AND':
            data['wires'][key] = get_value(data, data['gates'][key][1][0]) & get_value(data, data['gates'][key][1][1])
        elif data['gates'][key][0] == 'XOR':
            data['wires'][key] = get_value(data, data['gates'][key][1][0]) ^ get_value(data, data['gates'][key][1][1])
        elif data['gates'][key][0] == 'OR':
            data['wires'][key] = get_value(data, data['gates'][key][1][0]) | get_value(data, data['gates'][key][1][1])

    return data['wires'][key]

def find_switched_wires(data):
    local_data = deepcopy(data)
    gates_by_value = {
        'AND': {},
        'OR': {},
        'XOR': {}
    }
    for key in local_data['gates']:
        gates_by_value[local_data['gates'][key][0]][tuple(sorted(local_data['gates'][key][1]))] = key

    result = []
    pos = 2
    key = 'z' + str(pos).rjust(2, '0')
    
    preprev_inc = None
    while key in local_data['gates']:
        if 'z' + str(pos + 1).rjust(2, '0') not in local_data['gates']:
            break
        current_xor = gates_by_value['XOR'][('x' + str(pos).rjust(2, '0'), 'y' + str(pos).rjust(2, '0'))]
        prev_and = gates_by_value['AND'][('x' + str(pos - 1).rjust(2, '0'), 'y' + str(pos - 1).rjust(2, '0'))]
        prev_xor = gates_by_value['XOR'][('x' + str(pos - 1).rjust(2, '0'), 'y' + str(pos - 1).rjust(2, '0'))]
        if preprev_inc is None:
            preprev_inc = gates_by_value['AND'][('x' + str(pos - 2).rjust(2, '0'), 'y' + str(pos - 2).rjust(2, '0'))]

        prev_xor_and_preprev_inc_key = tuple(sorted([prev_xor, preprev_inc]))
        if prev_xor_and_preprev_inc_key not in gates_by_value['AND']:
            print("EXPECTED CONNECTION NOT FOUND: " + str(prev_xor_and_preprev_inc_key))
            exit()
        else:
            prev_xor_and_preprev_inc = gates_by_value['AND'][prev_xor_and_preprev_inc_key]

        prev_and_or_prev_xor_and_preprev_inc_key = tuple(sorted([prev_and, prev_xor_and_preprev_inc]))
        if prev_and_or_prev_xor_and_preprev_inc_key not in gates_by_value['OR']:
            print("EXPECTED CONNECTION NOT FOUND: " + str(prev_and_or_prev_xor_and_preprev_inc_key))
            exit()
        else:
            prev_and_or_prev_xor_and_preprev_inc = gates_by_value['OR'][tuple(sorted([prev_and, prev_xor_and_preprev_inc]))]

        final_key = tuple(sorted([current_xor, prev_and_or_prev_xor_and_preprev_inc]))
        if final_key not in gates_by_value['XOR']:
            check = data['gates']['z' + str(pos).rjust(2, '0')][1]
            if final_key[0] not in check:
                key1 = final_key[0]
            else:
                key1 = final_key[1]
            if check[0] not in final_key:
                key2 = check[0]
            else:
                key2 = check[1]
            switch_wires(data, gates_by_value, key1, key2, result)
            continue
        else:
            if gates_by_value['XOR'][final_key] != 'z' + str(pos).rjust(2, '0'):
                switch_wires(data, gates_by_value, 'z' + str(pos).rjust(2, '0'), gates_by_value['XOR'][final_key], result)

        pos += 1
        key = 'z' + str(pos).rjust(2, '0')
        preprev_inc = prev_and_or_prev_xor_and_preprev_inc

    return ",".join(sorted(result))

def switch_wires(data, gates_by_value, key1, key2, result):
    result.append(key1)
    result.append(key2)

    data1 = data['gates'][key1]
    data2 = data['gates'][key2]

    gates_by_value[data1[0]][tuple(sorted(data1[1]))] = key2
    gates_by_value[data2[0]][tuple(sorted(data2[1]))] = key1

def solve(data):
    """Solve the puzzle for the given input"""
    # Part 1
    solution1 = get_decimal(data)

    # Part 2
    solution2 = find_switched_wires(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    puzzle_data = puzzle_input(puzzle_input_file)
    solutions = solve(puzzle_data)
    print("\n".join(str(solution) for solution in solutions))