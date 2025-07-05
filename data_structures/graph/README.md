# Graph Data Structure

A **Graph** is a non-linear data structure consisting of a set of **nodes** (also called **vertices**) connected by **edges**. Unlike trees, graphs can represent complex relationships, including cycles and multiple connections between nodes. Graphs are fundamental in computer science for modeling networks, relationships, and solving a wide range of problems.

## 🧱 Basic Structure

Each graph consists of:

- **Vertices (Nodes)**: The entities or points in the graph.
- **Edges (Links)**: Connections between pairs of vertices.
- **Adjacency**: Two vertices are adjacent if they are connected by an edge.

Graphs can be:

- **Directed**: Edges have a direction (from one vertex to another).
- **Undirected**: Edges have no direction.
- **Weighted**: Edges have associated weights or costs.
- **Unweighted**: All edges are equal.

```python
# Example: Adjacency List Representation
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
```

## 🔄 Types of Graphs

1. **Undirected Graph**: Edges have no direction.
2. **Directed Graph (Digraph)**: Edges have direction.
3. **Weighted Graph**: Edges carry weights (e.g., distances, costs).
4. **Unweighted Graph**: All edges are equal.
5. **Cyclic Graph**: Contains cycles (paths that start and end at the same vertex).
6. **Acyclic Graph**: No cycles (e.g., Directed Acyclic Graphs - DAGs).
7. **Connected Graph**: There is a path between every pair of vertices.
8. **Disconnected Graph**: Not all vertices are connected.
9. **Complete Graph**: Every pair of vertices is connected by an edge.
10. **Sparse/Dense Graph**: Few/many edges relative to the number of vertices.

## ⚙️ Graph Representations

### 1. Adjacency List

- Each vertex stores a list of adjacent vertices.
- Space efficient for sparse graphs.

```python
adj_list = [
    [1, 2],    # Neighbors of vertex 0
    [0, 2],    # Neighbors of vertex 1
    [0, 1]     # Neighbors of vertex 2
]
```

### 2. Adjacency Matrix

- 2D array where `matrix[i][j]` is 1 (or weight) if there is an edge from i to j.
- Efficient for dense graphs.

```python
adj_matrix = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
```

## 🔑 Key Characteristics

- **Non-linear**: Can represent complex relationships.
- **Flexible**: Models social networks, maps, dependencies, etc.
- **Can have cycles**: Unlike trees, cycles are allowed.
- **Multiple representations**: Adjacency list, adjacency matrix, edge list.

## 🎯 Common Operations

| Operation         | Description                                 | Time Complexity (Adj. List) |
| ----------------- | ------------------------------------------- | --------------------------- |
| Add Vertex        | Add a new node                              | O(1)                        |
| Add Edge          | Connect two nodes                           | O(1)                        |
| Remove Vertex     | Remove a node and its edges                 | O(V + E)                    |
| Remove Edge       | Remove a connection                         | O(E)                        |
| Search/Traversal  | Visit nodes (BFS, DFS)                      | O(V + E)                    |
| Check Adjacency   | Are two nodes connected?                    | O(V)                        |

## 🔍 Traversal Algorithms

- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
- **Breadth-First Search (BFS)**: Explores all neighbors at the current depth before moving deeper.

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])
    return visited
```

## ✔️ Advantages

- Models complex relationships (networks, dependencies, routes).
- Flexible and powerful for many algorithms (shortest path, connectivity, etc.).
- Supports both sparse and dense data.

## ❌ Disadvantages

- Can be memory-intensive for dense graphs (adjacency matrix).
- Some algorithms are complex and require careful implementation.
- Visualization can be challenging for large graphs.

## 💡 Example Use Cases

- Social networks (friendship, followers)
- Web page links (internet graph)
- Transportation networks (roads, flights)
- Computer networks (routers, switches)
- Scheduling and dependency resolution (DAGs)
- Game maps and AI pathfinding

## 🎨 Visualization

**Undirected Graph**

```none
  0
 / \
1---2
```

**Directed Graph**

```none
0 → 1
↓   ↑
2 ←—
```

## 🚀 Implementation Example

```python
# Adjacency List
graph = [[] for _ in range(3)]
graph[0].extend([1, 2])
graph[1].extend([0, 2])
graph[2].extend([0, 1])

# Add edge (undirected)
def add_edge(adj_list, i, j):
    adj_list[i].append(j)
    adj_list[j].append(i)

# Display adjacency list
def display_adjacency_list(adj_list):
    for i, edges in enumerate(adj_list):
        print(f"{i}: {' -> '.join(str(edge) for edge in edges)}")
```

## 🌐 Language Implementations

### Python

- Use lists/dictionaries for adjacency lists.
- Use 2D lists for adjacency matrices.

### Java

- Use `ArrayList<ArrayList<Integer>>` for adjacency lists.
- Use 2D arrays for adjacency matrices.

---

**Key Insight:**  
Graphs are one of the most versatile and powerful data structures in computer science. Mastering graphs is essential for solving problems in networking, optimization, AI, and beyond. Understanding their representations and traversal algorithms is crucial for advanced