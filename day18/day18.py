# from collections import deque

# def read_input(file_path):
#     """Reads the input from a file and returns a list of tuples (x, y)."""
#     with open(file_path, 'r') as file:
#         return [tuple(map(int, line.strip().split(','))) for line in file.readlines()]

# def simulate_memory_fall(grid_size, byte_positions, num_bytes):
#     """Simulates the bytes falling and corrupting the grid."""
#     grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # 0 for safe, 1 for corrupted
#     for i in range(min(num_bytes, len(byte_positions))):
#         x, y = byte_positions[i]
#         grid[y][x] = 1  # Mark this position as corrupted
#     return grid

# def find_shortest_path(grid, start, end):
#     """Finds the shortest path from start to end using BFS."""
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
#     queue = deque([(start, 0)])  # (position, steps)
#     visited = set()
#     visited.add(start)

#     while queue:
#         (x, y), steps = queue.popleft()

#         # Check if we reached the end
#         if (x, y) == end:
#             return steps

#         # Explore neighbors
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy

#             if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] == 0:
#                 visited.add((nx, ny))
#                 queue.append(((nx, ny), steps + 1))

#     return -1  # Return -1 if no path exists

# def main():
#     # Constants
#     GRID_SIZE = 71  # 0 to 70
#     START = (0, 0)
#     END = (70, 70)
#     NUM_BYTES = 1024

#     # Read input
#     byte_positions = read_input("input.txt")

#     # Simulate memory corruption
#     grid = simulate_memory_fall(GRID_SIZE, byte_positions, NUM_BYTES)

#     # Find shortest path
#     shortest_path = find_shortest_path(grid, START, END)

#     if shortest_path != -1:
#         print(f"The minimum number of steps to reach the exit is: {shortest_path}")
#     else:
#         print("There is no valid path to the exit.")

# if __name__ == "__main__":
#     main()


from collections import deque

def is_path_blocked(grid, start, end, grid_size):
    """
    Check if there is a path from start to end using BFS.
    """
    queue = deque([start])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            return False  # Path exists
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny][nx] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return True  # Path is blocked

def find_first_blocking_byte(grid_size, bytes_positions):
    """
    Simulate bytes falling and find the first one that blocks all paths.
    """
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    
    for x, y in bytes_positions:
        grid[y][x] = 1  # Corrupt the position
        if is_path_blocked(grid, start, end, grid_size):
            return f"{x},{y}"

    return "Path never blocked"

def main():
    grid_size = 71  # Memory space is a 71x71 grid (0-70)
    
    # Read input from file
    with open("input.txt", "r") as file:
        bytes_positions = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]
    
    # Find the first byte that blocks the path
    result = find_first_blocking_byte(grid_size, bytes_positions)
    print(result)

if __name__ == "__main__":
    main()
