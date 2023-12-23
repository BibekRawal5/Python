class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
    def ask(self):
        return self.state
        
class Stack:
    def __init__(self):
        self.frontier = []
    
    def add(self,node):
        self.frontier.append(node)

    def remove(self):
        if not (self.empty()):
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        else:
            raise Exception("Frontier Empty")
        
    def empty(self):
        return len(self.frontier) == 0
        
    def length(self):
        return len(self.frontier)

class Queue:
    def __init__(self):
        self.frontier = []
    
    def add(self,node):
        self.frontier.append(node)

    def remove(self): 
        if not (self.empty()):
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        else:
            raise Exception("Frontier Empty")
        
    def empty(self):
        return len(self.frontier) == 0
        
    def length(self):
        return len(self.frontier)
    
        
class Maze:
    def __init__(self, filename):
        self.filename = filename.split('.')[0] + '.png'
        with open(filename) as fn:
            texts = fn.read()
            if texts.count('D') != 1:
                raise Exception("Error : D not in the Maze")
            if texts.count('K') != 1:
                raise Exception("Error : K not in the Maze")
            texts = texts.splitlines()
            
        self.start = None
        self.end = None
        self.walls = []
        self.path = []    
        self.width = len(max(texts))
        self.height = len(texts)
        
        for i in range(self.height):
            for j in range (self.width):
                if texts[i][j] == 'D':
                    self.end = (i,j)
                elif texts[i][j] == 'K':
                    self.start = (i,j)
                elif texts[i][j] == ' ':
                    self.path.append((i,j))
                else:
                    self.walls.append((i,j))
        
    
    def four_neighbours(self,state):
        i,j = state
        neighbours = [(i, j-1), (i, j+1), (i-1,j), (i+1,j)]
        result = []
        for r,c in neighbours:
            if 0 <= r < self.height and 0 <= c < self.width and (r,c) not in self.walls:
                result.append((r,c))
        return result
        

    def solution(self):
        start = Node(self.start, None)
        self.explored = []
        frontier = Queue()
        frontier.add(start)
        self.answer = []

        while True:
            node = frontier.remove()
            self.explored.append(node.state)
            if node.state == self.end:
                while node.parent != None:
                    self.answer.append(node.state)
                    node = node.parent
                return

            neighbours = self.four_neighbours(node.state)
            
            for neighbour in neighbours:
                if neighbour not in self.explored:
                    frontier.add(Node(neighbour, node))
            
                     
    def print_solution(self):
        if len(self.answer) == 0:
            raise Exception("No solution found")
        print(f"No of states explored: {len(self.explored)}")
        for r in range(self.height):
            for c in range(self.width):
                if (r,c) == self.end:
                    print('D', end='')
                elif (r,c) == self.start:
                    print('K', end='')
                elif (r,c) in self.answer:
                    print('*', end='')
                elif (r,c) in self.explored:
                    print('.', end='')
                elif (r,c) in self.path:
                    print(' ', end='')     
                else:
                    print('#', end='')        
            print()

    def output_image(self, show_solution=True, show_explored=True):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.answer[1:] if self.answer is not None else None
        for i in range(self.height):
            for j in range(self.width):

                if (i,j) in self.walls:
                    fill = (40, 40, 40)

                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                elif (i, j) == self.end:
                    fill = (0, 171, 28)

                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(self.filename)


filename = input("Enter the txt Maze filename with extension: ")
raze = Maze(filename)
raze.solution()
raze.print_solution() 
raze.output_image()

        