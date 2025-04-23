from collections import defaultdict

maze = defaultdict(list)
visited = set()
nodes = []
goal = 7
start = 0
nodes.append(start)
heuristic = {0:6, 1:3, 2:4, 3:2, 4:5, 5:5, 6:9, 7:0}


def neighbours():

    if len(nodes) == 0:
        return 1
    
    cn = min(nodes, key=lambda x: heuristic[x])
    visited.add(cn)

    print(cn, end="\t")
    
    if cn == goal:
        return 0

    
    for neighbour in maze[cn]:
        if neighbour not in visited:
            nodes.append(neighbour)
    
    neighbours()


def add_nodes(node, child):
    maze[node].append(child)

add_nodes(0, 2)
add_nodes(0, 1)
add_nodes(1, 2)
add_nodes(1, 3)
add_nodes(2, 4)
add_nodes(2, 5)
add_nodes(3, 6)
add_nodes(3, 7)


print(maze)
print(heuristic)
neighbours()

