from collections import deque

nodes = int(input())
pairs = int(input())

graph = {}

for _ in range(nodes):
    node_str, children_str = input().split(":")
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    queue = deque([source])
    visited = {source}
    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            queue.append(child)
            visited.add(child)
            parent[child] = node

    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    node = destination
    size = 0
    while node is not None:
        node = parent[node]
        size += 1

    print(f'{{{source}, {destination}}} -> {size - 1}')
