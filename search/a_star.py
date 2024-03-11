from collections import defaultdict

maze = defaultdict(dict)
visited = set()
nodes = []
goal = 7
start = 0
nodes.append(start)

def neighbours():

    if len(nodes) == 0:
        return 1
    
    cn = min()
    min_cost = maze[cn][]

    for node in nodes:
         for pos in maze[node].keys():
            if maze[node][pos] < maze[cn][pos]:
                cn = node
    
    print(cn, end="\t")
    
    if cn == goal:
        return 0

    
    for neighbour in maze[cn].keys():
        if neighbour not in visited:
            nodes.append(neighbour)
            if(neighbours() == 0):
                return 0

def add_nodes(node, child, cost):
    maze[node][child] = cost

add_nodes(0, 2, 5)
add_nodes(0, 1, 3)
add_nodes(1, 2, 5)
add_nodes(1, 3, 4)
add_nodes(2, 4, 8)
add_nodes(2, 5, 7)
add_nodes(3, 7, 8)
add_nodes(3, 6, 9)

print(maze)
neighbours()

