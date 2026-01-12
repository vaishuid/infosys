def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

dfs(graph, 'A')
