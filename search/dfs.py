from collections import defaultdict

maze = defaultdict(list)
visited = set()
stack = []
goal = 7
start = 0
stack.append(start)

def solve():

    if len(stack) == 0:
        return 1
    
    cn = stack.pop(-1)
    print(cn, end="\t")
    
    if cn == goal:
        return 0
    
    visited.add(cn)
    
    for neighbour in maze[cn]:
        if neighbour not in visited:
            stack.append(neighbour)
            visited.add(neighbour)
            if(solve() == 0):
                return 0

def add_nodes(node, child):
    maze[node].append(child)

add_nodes(0, 2)
add_nodes(0, 1)
add_nodes(1, 2)
add_nodes(1, 3)
add_nodes(2, 4)
add_nodes(2, 5)
add_nodes(3, 7)
add_nodes(3, 6)

solve()

