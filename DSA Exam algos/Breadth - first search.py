graph = {
        'A': ['C', 'B'],
        'B': ['D', 'A'],
        'C': ['E', 'A'],
        'E': ['F', 'C'],
        'D': ['F', 'B'],
        'F': ['G', 'E'],
        'G': ['F']
        }


def bfs(graph, start, end, k):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        #print(path, node)
        # path found
        if node == end:
            dist = len(path) - 1
            if dist > k:
                return 'NO'
            else:
                return 'YES'
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print(bfs(graph, 'B', 'E', 3))
