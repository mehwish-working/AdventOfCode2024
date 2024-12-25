from collections import deque
import sys

# Read the map from the input file
filename = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
with open(filename, 'r') as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

# Directions: Up, Down, Left, Right
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(start_i, start_j, visited):
    queue = deque()
    queue.append((start_i, start_j))
    visited[start_i][start_j] = True
    region_cells = []
    plant_type = grid[start_i][start_j]
    perimeter = 0

    while queue:
        i, j = queue.popleft()
        region_cells.append((i, j))
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            # Check if neighbor is out of bounds or different plant type
            if 0 <= ni < rows and 0 <= nj < cols:
                if grid[ni][nj] == plant_type:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
                else:
                    perimeter += 1
            else:
                perimeter += 1  # Edge of the grid
    area = len(region_cells)
    return area, perimeter

# Part One: Calculate total price using perimeter
visited = [[False]*cols for _ in range(rows)]
total_price_part1 = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            area, perimeter = bfs(i, j, visited)
            price_part1 = area * perimeter
            total_price_part1 += price_part1

print("Part One - Total price of fencing all regions:", total_price_part1)

#------------------------------------------------------------
# Part Two: Use the provided code to calculate number of sides
import collections

grid_lines = []
total_cells = 0

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        grid_lines.append(line)
        total_cells += len(line)

used = set()
out = 0

def p(a, b):
    return (a[0] + b[0], a[1] + b[1])

def invert(a):
    return (a[1], a[0])

def neg(a):
    return (-a[0], -a[1])

while len(used) < total_cells:
    for i in range(len(grid_lines)):
        for j in range(len(grid_lines[i])):
            if (i, j) not in used:
                current_region = set()
                borders = []
                num_borders = 0
                queue = [(i, j)]
                plant_type = grid_lines[i][j]
                while queue:
                    n = queue.pop()
                    current_region.add(n)
                    ii, jj = n
                    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        iii, jjj = ii + d[0], jj + d[1]
                        if (0 <= iii < len(grid_lines) and 0 <= jjj < len(grid_lines[iii]) and
                            grid_lines[iii][jjj] == plant_type):
                            if (iii, jjj) not in queue and (iii, jjj) not in current_region:
                                queue.append((iii, jjj))
                        else:
                            borders.append(((ii, jj), d))
                # Count the number of sides
                while borders:
                    pt, d = borders.pop()
                    flipped = invert(d)
                    pt2 = pt
                    # Remove consecutive edges in the same direction
                    while True:
                        pt2 = p(pt2, flipped)
                        if (pt2, d) in borders:
                            borders.remove((pt2, d))
                        else:
                            break
                    pt2 = pt
                    while True:
                        pt2 = p(pt2, neg(flipped))
                        if (pt2, d) in borders:
                            borders.remove((pt2, d))
                        else:
                            break
                    num_borders += 1  # Each group of contiguous edges in the same direction counts as one side

                area = len(current_region)
                price_part2 = area * num_borders
                out += price_part2
                # Mark region cells as used
                for n in current_region:
                    used.add(n)

print("Part Two - Total price of fencing all regions:", out)