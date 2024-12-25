from collections import defaultdict
from itertools import product
import multiprocessing as mp

def generate_next_secret(secret):
    result = secret ^ (secret * 64)
    result %= 16777216
    result ^= (result // 32)
    result %= 16777216
    result ^= (result * 2048)
    result %= 16777216
    return result

def get_prices_and_changes(initial_secret, length=2000):
    prices = []
    changes = []
    secret = initial_secret
    last_price = secret % 10
    
    for _ in range(length):
        secret = generate_next_secret(secret)
        price = secret % 10
        prices.append(price)
        changes.append(price - last_price)
        last_price = price
    
    return prices, changes

def find_sequence_value(changes, sequence, prices):
    for i in range(len(changes) - 3):
        if changes[i:i+4] == sequence:
            return prices[i+3]
    return 0

def evaluate_sequence_batch(args):
    sequence, all_changes, all_prices = args
    total = 0
    for changes, prices in zip(all_changes, all_prices):
        score = find_sequence_value(changes, sequence, prices)
        if score:
            total += score
    return (sequence, total)

def solve():
    with open('input.txt', 'r') as f:
        secrets = [int(x) for x in f]
    
    # Part 1
    part1_sum = 0
    for secret in secrets:
        current = secret
        for _ in range(2000):
            current = generate_next_secret(current)
        part1_sum += current
    print(f"The sum of the 2000th secret numbers is: {part1_sum}")
    
    # Part 2 - Optimized
    all_prices_changes = [get_prices_and_changes(secret) for secret in secrets]
    all_prices = [p for p, _ in all_prices_changes]
    all_changes = [c for _, c in all_prices_changes]
    
    # Generate likely sequences based on actual changes
    change_frequencies = defaultdict(int)
    for changes in all_changes:
        for i in range(len(changes) - 3):
            change_frequencies[tuple(changes[i:i+4])] += 1
    
    # Sort sequences by frequency and take top 1000
    common_sequences = sorted(change_frequencies.items(), key=lambda x: x[1], reverse=True)[:1000]
    sequences = [list(seq) for seq, _ in common_sequences]
    
    # Parallel processing
    with mp.Pool() as pool:
        args = [(seq, all_changes, all_prices) for seq in sequences]
        results = pool.map(evaluate_sequence_batch, args)
    
    best_sequence, max_bananas = max(results, key=lambda x: x[1])
    print(f"Maximum Bananas: {max_bananas}")

if __name__ == "__main__":
    solve()