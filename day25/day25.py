def parse_schematic(lines):
    """
    Given 7 lines (strings) of length 5 each,
    determine if it's a lock or a key, then convert
    to a list of column heights [h0, h1, h2, h3, h4].
    
    For locks (top row = '#', bottom row = '.'):
      - For each column, count consecutive '#' from the top.
        That count is the pin 'height'.
        
    For keys (top row = '.', bottom row = '#'):
      - For each column, count consecutive '#' from the bottom.
        That count is the pin 'height'.
    """

    # Distinguish lock vs key by top/bottom row
    top_row = lines[0]
    bottom_row = lines[-1]

    # Each line has 5 characters, each schematic is 7 lines tall
    # Let's gather column heights
    heights = [0] * 5  # one integer per column

    if top_row[0] == '#':
        # This is a lock: pin heights from the top down
        for col in range(5):
            h = 0
            for row in range(7):
                if lines[row][col] == '#':
                    h += 1
                else:
                    break
            heights[col] = h
    else:
        # This is a key: pin heights from the bottom up
        for col in range(5):
            h = 0
            for row in range(6, -1, -1):  # bottom to top
                if lines[row][col] == '#':
                    h += 1
                else:
                    break
            heights[col] = h

    # Return (type, heights)
    # type is either 'lock' or 'key'
    schematic_type = 'lock' if top_row[0] == '#' else 'key'
    return schematic_type, heights


def fits(lock_heights, key_heights):
    """
    Return True if lock and key do not overlap
    in any column. In other words, lock_heights[i] + key_heights[i] <= 7
    for i in [0..4].
    """
    for lh, kh in zip(lock_heights, key_heights):
        if lh + kh > 7:
            return False
    return True


def main():
    # Read the entire input file
    with open("input.txt", "r") as f:
        all_lines = [line.rstrip('\n') for line in f]

    # Clean out any empty lines that might just be separators
    # (Some puzzle inputs have blank lines between groups.)
    filtered_lines = [ln for ln in all_lines if ln.strip() != '']

    # Now parse every consecutive group of 7 lines
    # Each group is one schematic (7 lines of length 5)
    # So we'll step by 7 in the filtered lines
    # If the puzzle doesn't have extra blank lines, that’s fine—same logic works.

    locks = []
    keys = []

    # We assume the file is well-formed with full 7-line blocks.
    for i in range(0, len(filtered_lines), 7):
        block = filtered_lines[i:i+7]
        # parse the block
        schematic_type, heights = parse_schematic(block)
        if schematic_type == 'lock':
            locks.append(heights)
        else:
            keys.append(heights)

    # Now we have a list of locks and a list of keys
    count_fits = 0
    for lock in locks:
        for key in keys:
            if fits(lock, key):
                count_fits += 1

    # Print the result
    print(f"Number of unique lock/key pairs that fit:{count_fits}")


if __name__ == "__main__":
    main()