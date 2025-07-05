"""
Breath First Search (BFS) is an algorithm for traversing or searching tree or graph data structures.

It starts at a selected node (often called the 'source' or 'root') and explores all of its neighbors
at the present depth prior to moving on to nodes at the next depth level.

It is often used to find the shortest path in an unweighted graph.
This implementation handles disconnected graphs by iterating through all nodes.
It returns a list of nodes that are reachable from the source node.
It is a non-recursive implementation using a queue.
It is also known as a level-order traversal.
It is important to note that this implementation does not handle cycles.

Complexity:
- Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
- Space Complexity: O(V), where V is the number of vertices (for the visited array and queue).


"""
from typing import List


def bfs(graph: List[List], start:int=0) -> List[int]:
    """"
    This implementation of Depth First Search (DFS) takes a source node as input
    and returns a list of nodes that are reachable from the source node.

    However, it would not return all nodes in case of a disconnected graph.


    1.- Initialization: Enqueue the starting node and mark it as visited.

    2.- While the queue is not empty:
        a. Dequeue a node from the queue.
        b. Process the node (e.g., print it).
        c. Enqueue all unvisited neighbors of the node and mark them as visited.

    3.- Repeat until all nodes are processed (meaning the queue is empty).
    """

    # Get the number of vertices in the graph
    num_vertices = len(graph)

    # Create an array to store the traversal
    result = []

    # Create a queue for BFS
    queue = []

    # Create a visited array to keep track of visited nodes
    visited = [False] * num_vertices

    # Mark source node as visited and enqueue it
    visited[0] = True
    queue.append(start)

    # While the queue is not empty
    while queue:
        # Dequeue a vertex from the queue and add it to the result
        vertex = queue.pop(0)
        result.append(vertex)

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            # If the neighbor has not been visited, mark it as visited and enqueue it
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result

def bfs_of_graph(graph: List[List], visited: List[bool],
                 result: List[int], start: int = 0) -> List[int]:
    """
    This implementation of Breadth First Search (BFS) takes a source node as input
    and returns a list of nodes that are reachable from the source node.
    It handles disconnected graphs by iterating through all nodes.
    """

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    visited[start] = True
    queue.append(start)

    # While the queue is not empty
    while queue:
        # Dequeue a vertex from the queue and add it to the result
        vertex = queue.pop(0)
        result.append(vertex)

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            # If the neighbor has not been visited, mark it as visited and enqueue it
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result


def dfs_disconnected(graph: List[List]) -> List[int]:
    """
    This implementation of Depth First Search (DFS) takes a source node as input
    and returns a list of nodes that are reachable from the source node.
    It handles disconnected graphs by iterating through all nodes.

    """
    # Get the number of vertices in the graph
    num_vertices = len(graph)

    # Create an array to store the traversal
    result = []

    # Create a visited array to keep track of visited nodes
    visited = [False] * num_vertices

    # Perform DFS for each vertex
    for vertex in range(num_vertices):
        if not visited[vertex]:
            bfs_of_graph(graph, visited, result, vertex)

    return result