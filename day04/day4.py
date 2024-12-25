# Part 01
def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Diagonal up-left
        (-1, 1),  # Diagonal up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(start_x, start_y, dir_x, dir_y):
        for i in range(word_len):
            nx, ny = start_x + i * dir_x, start_y + i * dir_y
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dir_x, dir_y in directions:
                if find_word(x, y, dir_x, dir_y):
                    count += 1
    return count

# Read input from input.txt
with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]


# Call the function and print the result
result = count_xmas(grid)
print("Total occurrences of 'XMAS':", result)

# --------------------------------------
# Part 02
# Read the grid from the input file
with open('input.txt') as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])
word = "XMAS"
word_len = len(word)
count_part1 = 0

# Directions: N, NE, E, SE, S, SW, W, NW
directions = [(-1, 0),  (-1, 1), (0, 1),  (1, 1),
              (1, 0),   (1, -1), (0, -1), (-1, -1)]
def check_x_mas(i, j):
    # Possible variations of "MAS" and "SAM"
    mas_variations = ["MAS", "SAM"]
    count = 0
    # Check all combinations of diagonals
    for diag1 in mas_variations:
        for diag2 in mas_variations:
            match = True
            # First diagonal (\)
            for k in range(3):
                x = i - 1 + k
                y = j - 1 + k
                if not (0 <= x < rows and 0 <= y < cols and grid[x][y] == diag1[k]):
                    match = False
                    break
            if not match:
                continue
            # Second diagonal (/)
            for k in range(3):
                x = i - 1 + k
                y = j + 1 - k
                if not (0 <= x < rows and 0 <= y < cols and grid[x][y] == diag2[k]):
                    match = False
                    break
            if match:
                count += 1
    return count

count_part2 = 0

# Since the 'X' is 3x3, we need to avoid edges
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        count_part2 += check_x_mas(i, j)

print("Total occurrences of X-MAS:", count_part2)