# Read the grid from the input file
grid = [line.strip() for line in open('input.txt') if line.strip()]
N, M = len(grid), len(grid[0])
nodes = {}

# Collect antenna positions grouped by frequency
for i in range(N):
    for j in range(M):
        if grid[i][j] != '.':
            nodes[grid[i][j]] = nodes.get(grid[i][j], []) + [(i, j)]

# Initialize sets to store antinode positions for both methods
antinodes_method1 = set()
antinodes_method2 = set()

# Method 1
for k in nodes:
    node_list = nodes[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            # Consider both directions for node pairs
            for node1, node2 in [(node_list[i], node_list[j]), (node_list[j], node_list[i])]:
                x1, y1 = node1
                x2, y2 = node2
                dx, dy = x2 - x1, y2 - y1
                newx, newy = x2 + dx, y2 + dy
                antinodes_method1.add((x2, y2))
                # Continue adding antinodes along the line until out of bounds
                while 0 <= newx < N and 0 <= newy < M:
                    antinodes_method1.add((newx, newy))
                    newx += dx
                    newy += dy

# Method 2
for k in nodes:
    node_list = nodes[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            node1, node2 = node_list[i], node_list[j]
            x1, y1 = node1
            x2, y2 = node2
            # First antinode
            newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)
            if 0 <= newx < N and 0 <= newy < M:
                antinodes_method2.add((newx, newy))
            # Swap node1 and node2 for the second antinode
            x1, y1 = node2
            x2, y2 = node1
            newx, newy = x2 + (x2 - x1), y2 + (y2 - y1)
            if 0 <= newx < N and 0 <= newy < M:
                antinodes_method2.add((newx, newy))




print("Part 1: ", len(antinodes_method2))
print("Part 2: ", len(antinodes_method1))