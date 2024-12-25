# Part 01
from collections import deque
def read_map(filename):
    """Read the topographic map from a file."""
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def bfs_find_reachable_nines(start_x, start_y, topographic_map):
    """Perform BFS to count reachable height-9 positions from a trailhead."""
    rows, cols = len(topographic_map), len(topographic_map[0])
    queue = deque([(start_x, start_y, 0)])  # (x, y, current height)
    visited = set()
    reachable_nines = 0

    while queue:
        x, y, current_height = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # If the position has height 9, increment the reachable count
        if topographic_map[x][y] == 9:
            reachable_nines += 1
            continue

        # Explore neighbors (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                (nx, ny) not in visited and
                topographic_map[nx][ny] == current_height + 1
            ):
                queue.append((nx, ny, topographic_map[nx][ny]))

    return reachable_nines

def calculate_trailhead_scores(topographic_map):
    """Calculate scores for all trailheads (positions with height 0)."""
    rows, cols = len(topographic_map), len(topographic_map[0])
    total_score = 0

    for r in range(rows):
        for c in range(cols):
            if topographic_map[r][c] == 0:  # Identify trailhead
                total_score += bfs_find_reachable_nines(r, c, topographic_map)

    return total_score

def main():
    # Read the topographic map from file
    filename = "input.txt"
    topographic_map = read_map(filename)
    
    # Calculate total trailhead scores
    total_score = calculate_trailhead_scores(topographic_map)
    print("Sum of all trailhead scores:", total_score)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------
# Part 02
def read_map(filename):
    """Reads the map from the file and converts it into a 2D list."""
    with open(filename, "r") as file:
        return [list(map(int, line.strip())) for line in file]

def find_trails(x, y, current_height, topographic_map, visited):
    """
    Recursively finds all distinct hiking trails starting at (x, y).
    A trail is valid if it incrementally increases in height by 1 and ends at height 9.
    """
    rows, cols = len(topographic_map), len(topographic_map[0])
    if not (0 <= x < rows and 0 <= y < cols):  # Check boundaries.
        return 0
    if (x, y) in visited:  # Avoid revisiting the same cell in the current trail.
        return 0
    if topographic_map[x][y] != current_height:  # Height must match expected.
        return 0
    if topographic_map[x][y] == 9:  # If we reach height 9, we have a complete trail.
        return 1

    # Mark the current cell as visited.
    visited.add((x, y))

    # Explore all four directions.
    total_trails = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        total_trails += find_trails(x + dx, y + dy, current_height + 1, topographic_map, visited)

    # Unmark the current cell after exploring.
    visited.remove((x, y))

    return total_trails

def calculate_trailhead_ratings(topographic_map):
    """
    Calculates the sum of all trailhead ratings.
    A trailhead is any cell with a height of 0.
    Its rating is the number of distinct hiking trails that begin at that position.
    """
    rows, cols = len(topographic_map), len(topographic_map[0])
    total_rating = 0

    for r in range(rows):
        for c in range(cols):
            if topographic_map[r][c] == 0:  # Only consider cells with height 0.
                total_rating += find_trails(r, c, 0, topographic_map, set())

    return total_rating

def main():
    # Read the map from the file.
    filename = "input.txt"
    topographic_map = read_map(filename)

    # Calculate and print the sum of all trailhead ratings.
    total_rating = calculate_trailhead_ratings(topographic_map)
    print("Sum of all trailhead ratings:", total_rating)

if __name__ == "__main__":
    main()
