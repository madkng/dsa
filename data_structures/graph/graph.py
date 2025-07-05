r"""
A graph is a non-linear data structure consisting of a set of
 nodes (or vertices) connected by edges.

Graphs can be directed or undirected, weighted or unweighted,
and can represent various relationships between entities.

They are widely used in computer science for modeling networks,
relationships, and various algorithms.

The difference between a graph and a tree is that
a three can only represent hierarchical relationships,
while a graph can represent more complex relationships,
including cycles and multiple connections between nodes.

Example situations where graphs are used include:
- Social networks (e.g., Facebook, Twitter)
- Transportation networks (e.g., road maps, flight routes)
- Computer networks (e.g., internet topology)

Representation of a graph are mainly done using two methods:
1. Adjacency List: A list where each node has a list of its adjacent nodes
    An adjacency

2. Adjacency Matrix: A 2D array where the cell at row i and column j indicates
    whether there is an edge from node i to node j
    An  adjacency matrix is a way of representing a graph as a matrix of booleans or weights.
    Let's assume there are n vertices in the graph, so we would need to create a
    2D matrix ajdMat[n][n] having dimensions n x n.
        - If there is an edge from vertex i to vertex j,
          then ajdMat[i][j] = 1 (or the weight of the edge)

        - If there is no edge from vertex i to vertex j, then ajdMat[i][j] = 0

    # Example of an adjacency matrix for an undirected graph with 4 vertices or nodes:
    0 |  1 |  2
    -----------
   0|0|  1 | 1
   ------------
   1|1|  0 | 1
   ------------
   2|1|  1 | 0

   Graph representation:
   1 - 2
    \/
    0

Traversals:
- Depth First Search (DFS): A traversal method that explores as far as possible
  along each branch before backtracking.

- Breadth First Search (BFS): A traversal method that explores all neighbors at the present
  depth prior to moving on to nodes at the next depth level.

"""

from typing import List


def add_edge_adj_mat(adj_matrix, i, j, weight=1):
    """Add an edge to the adjacency matrix."""

    # Add the edge from i to j with the specified weight
    adj_matrix[i][j] = weight
    adj_matrix[j][i] = weight  # For undirected graph

def add_edge_adj_list(adj_list, i, j):
    """Add an edge to the adjacency list"""
    adj_list[i].append(j)
    adj_list[j].append(i)  # For undirected graph

def display_adjacency_matrix(adj_matrix):
    """Display the adjacency matrix."""
    for row in adj_matrix:
        print(" | ".join(str(cell) for cell in row))

def display_adjacency_list(adj_list):
    """Display the adjacency list."""
    for i, edges in enumerate(adj_list):
        print(f"{i}: {' -> '.join(str(edge) for edge in edges)}")

def create_adjacency_matrix(num_vertices):
    """Create an adjacency matrix for a graph with the specified number of vertices."""
    return [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

def create_adjacency_list(num_vertices):
    """Create an adjacency list for a graph with the specified number of vertices."""
    return [[] for _ in range(num_vertices)]

if __name__ == '__main__':
    VERTICES = 5
    matrix = create_adjacency_matrix(VERTICES)

    # Example of an adjacency matrix for an undirected graph with 3 vertices or nodes:
    # add_edge_adj_mat(matrix, 0, 1)
    # add_edge_adj_mat(matrix, 0, 2)
    # add_edge_adj_mat(matrix, 1, 2)

    # display_adjacency_matrix(matrix)

    # Example of an adjacency list for an undirected graph with 4 vertices or nodes:
    adj_list = [[1, 2], [0], [0], [4], [3, 5], [4]]
    # Display the adjacency list
    print("Adjacency List:")
    display_adjacency_list(adj_list)
