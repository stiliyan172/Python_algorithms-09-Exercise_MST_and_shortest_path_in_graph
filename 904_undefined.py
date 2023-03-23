# Bellman - Ford algorithm with possible negative edges

nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    graph.append((first, second, weight))

source = int(input())
destination = int(input())

distance = [float('ínf')] * (nodes + 1)
distance[source] = 0

for _ in range(nodes - 1):
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue
        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
