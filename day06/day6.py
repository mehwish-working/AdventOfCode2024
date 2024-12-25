# Read the map from the input file
with open('input.txt', 'r') as f:
    grid = [list(line.rstrip('\n')) for line in f]

rows = len(grid)
cols = len(grid[0])

# Directions: Up, Right, Down, Left
directions = ['^', '>', 'v', '<']
dx = [-1, 0, 1, 0]  # Change in row for each direction
dy = [0, 1, 0, -1]  # Change in column for each direction

# Find the guard's starting position and facing direction
start_x, start_y, dir_idx = None, None, None
for i in range(rows):
    for j in range(cols):
        if grid[i][j] in directions:
            start_x, start_y = i, j
            dir_idx = directions.index(grid[i][j])
            break
    if start_x is not None:
        break

# Part One: Simulate the guard's movement and count distinct positions visited
def simulate_guard(grid, start_x, start_y, dir_idx):
    x, y = start_x, start_y
    visited = set()
    visited.add((x, y))
    rows = len(grid)
    cols = len(grid[0])
    while True:
        # Next position
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        # Check if next position is outside the map
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            break  # Guard leaves the map

        # Check if there's an obstacle
        if grid[nx][ny] == '#':
            # Turn right 90 degrees
            dir_idx = (dir_idx + 1) % 4
        else:
            # Move forward
            x, y = nx, ny
            visited.add((x, y))

    return visited

visited_positions = simulate_guard(grid, start_x, start_y, dir_idx)
print("Part One - Total distinct positions visited:", len(visited_positions))

# Part Two: Find all positions where adding an obstruction causes the guard to loop
def simulate_guard_with_loop(grid, start_x, start_y, dir_idx):
    x, y = start_x, start_y
    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    while True:
        # Check if the guard is revisiting a state (position and direction)
        state = (x, y, dir_idx)
        if state in visited:
            return True  # Guard is in a loop
        visited.add(state)

        # Next position
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        # Check if next position is outside the map
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            return False  # Guard leaves the map

        # Check if there's an obstacle
        if grid[nx][ny] == '#':
            # Turn right 90 degrees
            dir_idx = (dir_idx + 1) % 4
        else:
            # Move forward
            x, y = nx, ny

possible_positions = 0

# We cannot place an obstruction at the guard's starting position
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '.' and (i, j) != (start_x, start_y):
            # Copy the grid and place an obstruction at (i, j)
            grid_copy = [row[:] for row in grid]
            grid_copy[i][j] = '#'

            # Simulate the guard's movement with the obstruction
            if simulate_guard_with_loop(grid_copy, start_x, start_y, dir_idx):
                possible_positions += 1

print("Part Two - Total possible obstruction positions:", possible_positions)