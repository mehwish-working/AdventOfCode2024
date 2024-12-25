from collections import Counter

def simulate_blinks(stones, blinks):
    """
    Simulate the stone transformations for a given number of blinks.
    stones: List of initial stone numbers.
    blinks: Total number of blinks to simulate.
    Returns the total number of stones after the given blinks.
    """
    # Use a counter to track stone frequencies
    stone_counts = Counter(stones)

    for _ in range(blinks):
        new_stone_counts = Counter()

        for stone, count in stone_counts.items():
            if stone == 0:
                # Rule 1: If the stone is 0, it becomes 1
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                # Rule 2: Split into two stones
                num_str = str(stone)
                mid = len(num_str) // 2
                left = int(num_str[:mid]) if mid > 0 else 0
                right = int(num_str[mid:]) if mid < len(num_str) else 0
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                # Rule 3: Multiply by 2024
                new_stone_counts[stone * 2024] += count

        stone_counts = new_stone_counts

    # Total number of stones
    return sum(stone_counts.values())

def main():
    try:
        # Read input from file
        with open("input.txt", "r") as file:
            stones = list(map(int, file.read().strip().split()))
        
        # Number of blinks
        blinks = 75

        # Calculate total stones after blinks
        total_stones = simulate_blinks(stones, blinks)

        print(f"Number of stones after {blinks} blinks: {total_stones}")

    except FileNotFoundError:
        print("Error: The file 'input.txt' was not found.")
    except ValueError:
        print("Error: Invalid data in the file.")

if __name__ == "__main__":
    main()
