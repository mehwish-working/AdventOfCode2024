import sys
import re
import heapq
from collections import defaultdict, Counter, deque
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]  # up right down left

def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

def solve_maze(filename):
    try:
        with open(filename, 'r') as f:
            D = f.read().strip()
    except FileNotFoundError:
        print(f"Error: Could not find input file {filename}")
        return
    
    G = D.split('\n')
    R = len(G)
    C = len(G[0])
    G = [[G[r][c] for c in range(C)] for r in range(R)]

    # Find start and end positions
    sr = sc = er = ec = None
    for r in range(R):
        for c in range(C):
            if G[r][c] == 'S':
                sr,sc = r,c
            if G[r][c] == 'E':
                er,ec = r,c

    if None in (sr, sc, er, ec):
        print("Error: Could not find start (S) or end (E) position")
        return

    # Part 1: Find shortest path
    Q = []
    SEEN = set()
    heapq.heappush(Q, (0,sr,sc,1))
    DIST = {}
    best = None
    
    while Q:
        d,r,c,dir = heapq.heappop(Q)
        if (r,c,dir) not in DIST:
            DIST[(r,c,dir)] = d
        if r==er and c==ec and best is None:
            best = d
        if (r,c,dir) in SEEN:
            continue
        SEEN.add((r,c,dir))
        dr,dc = DIRS[dir]
        rr,cc = r+dr,c+dc
        if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
            heapq.heappush(Q, (d+1, rr,cc,dir))
        heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
        heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))

    # Part 2: Find all tiles on optimal paths
    Q = []
    SEEN = set()
    for dir in range(4):
        heapq.heappush(Q, (0,er,ec,dir))
    DIST2 = {}
    
    while Q:
        d,r,c,dir = heapq.heappop(Q)
        if (r,c,dir) not in DIST2:
            DIST2[(r,c,dir)] = d
        if (r,c,dir) in SEEN:
            continue
        SEEN.add((r,c,dir))
        dr,dc = DIRS[(dir+2)%4]
        rr,cc = r+dr,c+dc
        if 0<=cc<C and 0<=rr<R and G[rr][cc] != '#':
            heapq.heappush(Q, (d+1, rr,cc,dir))
        heapq.heappush(Q, (d+1000, r,c,(dir+1)%4))
        heapq.heappush(Q, (d+1000, r,c,(dir+3)%4))

    OK = set()
    for r in range(R):
        for c in range(C):
            for dir in range(4):
                if (r,c,dir) in DIST and (r,c,dir) in DIST2 and DIST[(r,c,dir)] + DIST2[(r,c,dir)] == best:
                    OK.add((r,c))

    return best, len(OK)

if __name__ == "__main__":
    filename = 'input.txt'
    result = solve_maze(filename)
    if result:
        best_score, optimal_tiles = result
        print(f"Part 1 - Minimum score: {best_score}")
        print(f"Part 2 - Tiles on optimal paths: {optimal_tiles}")