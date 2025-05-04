from collections import deque

def DFS(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

def BFS(graph, queue, visited):
    if not queue:
        return
    next_level = deque()
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                next_level.append(neighbor)
    BFS(graph, next_level, visited)

def main():
    graph = {}
    n = int(input("Enter the no of nodes: "))
    e = int(input("Enter the no of edges: "))
    print("Enter the edges in format: node1 node2")
    for _ in range(e):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    start_node = input("Enter the starting node: ")

    print("Depth First Search:")
    DFS(graph, start_node)
    print()  
    visited_bfs = set([start_node])
    queue = deque([start_node])

    print("Breadth First Search:")
    BFS(graph, queue, visited_bfs)
    print()  

main()
