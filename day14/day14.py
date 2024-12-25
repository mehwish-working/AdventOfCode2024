# PART 1

# def parse_input(file_path):
#     """Parses the input file to extract positions and velocities."""
#     robots = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             parts = line.strip().split()
#             p = tuple(map(int, parts[0][2:].strip(',').split(',')))  # Extract position
#             v = tuple(map(int, parts[1][2:].split(',')))            # Extract velocity
#             robots.append((p, v))
#     return robots

# def update_position(position, velocity, width, height):
#     """Updates the position of a robot based on its velocity and wraps around if needed."""
#     new_x = (position[0] + velocity[0]) % width
#     new_y = (position[1] + velocity[1]) % height
#     return (new_x, new_y)

# def simulate_motion(robots, seconds, width, height):
#     """Simulates the motion of robots for the given number of seconds."""
#     for _ in range(seconds):
#         robots = [(update_position(p, v, width, height), v) for p, v in robots]
#     return robots

# def calculate_safety_factor(robots, width, height):
#     """Calculates the safety factor based on robot distribution in quadrants."""
#     # Divide space into four quadrants
#     mid_x = width // 2
#     mid_y = height // 2

#     quadrants = [0, 0, 0, 0]  # Quadrants: [top-left, top-right, bottom-left, bottom-right]

#     for position, _ in robots:
#         x, y = position
#         if x == mid_x or y == mid_y:  # Ignore robots on the middle lines
#             continue
#         if x < mid_x and y < mid_y:
#             quadrants[0] += 1  # Top-left
#         elif x >= mid_x and y < mid_y:
#             quadrants[1] += 1  # Top-right
#         elif x < mid_x and y >= mid_y:
#             quadrants[2] += 1  # Bottom-left
#         else:
#             quadrants[3] += 1  # Bottom-right

#     # Calculate safety factor as the product of robot counts in all quadrants
#     safety_factor = 1
#     for count in quadrants:
#         safety_factor *= count

#     return safety_factor

# if __name__ == "__main__":
#     # Input file and grid dimensions
#     input_file = "input.txt"
#     grid_width = 101
#     grid_height = 103

#     # Read and parse input
#     robots = parse_input(input_file)

#     # Simulate motion for 100 seconds
#     robots = simulate_motion(robots, 100, grid_width, grid_height)

#     # Calculate and print safety factor
#     safety_factor = calculate_safety_factor(robots, grid_width, grid_height)
#     print("Safety Factor:", safety_factor)

# ------------------------------------------------------------------------

# PART 1 and 2

from rich import print

def parse_input(data):
    robots = []
    for line in data:
        p, v = line.strip().split(' ')
        px, py = map(int, p[2:].split(','))
        vx, vy = map(int, v[2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots

def move_robot(position, velocity, width, height):
    x, y = position
    vx, vy = velocity
    x = (x + vx) % width
    y = (y + vy) % height
    return (x, y)

def simulate_robots(robots, width, height, seconds):
    for _ in range(seconds):
        robots = [(move_robot(p, v, width, height), v) for p, v in robots]
    return robots

def count_robots_in_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]
    for (x, y), _ in robots:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1
    return quadrants

def check_christmas_tree_pattern(robots, width, height):
    tree_pattern = [
        "....#....",
        "...###...",
        "..#####..",
        ".#######.",
        "#########",
        "....#....",
        "....#...."
    ]

    grid = [['.' for _ in range(width)] for _ in range(height)]
    for (x, y), _ in robots:
        grid[y][x] = '#'

    pattern_height = len(tree_pattern)
    pattern_width = len(tree_pattern[0])

    for y in range(height - pattern_height + 1):
        for x in range(width - pattern_width + 1):
            match = True
            for py in range(pattern_height):
                for px in range(pattern_width):
                    if tree_pattern[py][px] == '#' and grid[y + py][x + px] != '#':
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
    return False

def find_easter_egg(data):
    width, height = 101, 103
    robots = parse_input(data)
    seconds = 0
    while True:
        robots = simulate_robots(robots, width, height, 1)
        seconds += 1
        if check_christmas_tree_pattern(robots, width, height):
            return seconds

def solve(data):
    width, height = 101, 103
    robots = parse_input(data)
    robots = simulate_robots(robots, width, height, 100)
    quadrants = count_robots_in_quadrants(robots, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

def main():
    # Update this to the path of your input file
    file_path = 'input.txt'

    # Read the input data from the file
    with open(file_path, 'r') as file:
        data = file.readlines()

    print("Safety Factor:", solve(data))
    print("Seconds to Easter Egg:", find_easter_egg(data))

if __name__ == '__main__':
    main()
