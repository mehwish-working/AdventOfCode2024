# Part 01
# Function to read connections from input file
# def read_connections(filename):
#     connections = []
#     with open(filename, "r") as file:
#         for line in file:
#             a, b = line.strip().split("-")
#             connections.append((a, b))
#     return connections

# # Build an adjacency list for the graph
# def build_adjacency_list(connections):
#     graph = {}
#     for a, b in connections:
#         if a not in graph:
#             graph[a] = set()
#         if b not in graph:
#             graph[b] = set()
#         graph[a].add(b)
#         graph[b].add(a)
#     return graph

# # Find all sets of three interconnected computers
# def find_triplets(graph):
#     triplets = set()
#     for node in graph:
#         neighbors = graph[node]
#         for neighbor1 in neighbors:
#             for neighbor2 in neighbors:
#                 if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
#                     triplet = tuple(sorted([node, neighbor1, neighbor2]))
#                     triplets.add(triplet)
#     return triplets

# # Filter triplets containing a computer whose name starts with 't'
# def filter_triplets_with_t(triplets):
#     return [triplet for triplet in triplets if any(computer.startswith("t") for computer in triplet)]

# # Main function
# def main():
#     connections = read_connections("input.txt")
#     graph = build_adjacency_list(connections)
#     triplets = find_triplets(graph)
#     triplets_with_t = filter_triplets_with_t(triplets)

#     print("Total triplets with at least one computer starting with 't':", len(triplets_with_t))
#     print("Triplets:", triplets_with_t)

# if __name__ == "__main__":
#     main()



# -----------------------------------------------------
# Part 02
from collections import defaultdict

def read_input(file_name):
    """Reads input from the specified file."""
    with open(file_name, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def bron_kerbosch(graph, r, p, x, cliques):
    """Bron-Kerbosch algorithm to find maximal cliques."""
    if not p and not x:
        cliques.append(r)
        return
    for v in list(p):
        bron_kerbosch(
            graph, 
            r.union({v}), 
            p.intersection(graph[v]), 
            x.intersection(graph[v]), 
            cliques
        )
        p.remove(v)
        x.add(v)

def find_maximal_cliques(graph):
    """Finds all maximal cliques in the graph."""
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    return cliques

def find_largest_clique(cliques):
    """Finds the largest clique among all cliques."""
    return max(cliques, key=len)

def generate_password(clique):
    """Generates the password from the largest clique."""
    return ",".join(sorted(clique))

def main():
    # Input file name
    input_file = "input.txt"

    # Read input connections
    connections = read_input(input_file)

    # Build the adjacency list
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

    # Find all maximal cliques
    cliques = find_maximal_cliques(graph)

    # Find the largest clique
    largest_clique = find_largest_clique(cliques)

    # Generate the password
    password = generate_password(largest_clique)
    print(f"Password to the LAN party: {password}")

if __name__ == "__main__":
    main()
