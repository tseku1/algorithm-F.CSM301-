# from collections import deque

def dfs_path(graph, start, goal):
    stack = [start]
    parent = {start: None}
    seen = {start}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        for neighbor in graph.get(current, {}):
            if neighbor not in seen:
                seen.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    if goal not in parent:
        return []

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path
