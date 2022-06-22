import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
maze = []

for i in range(n):
    row = sys.stdin.readline().strip()
    maze.append([])
    for j in row:
        maze[i].append(int(j))
        

def find_road(row, col):
    possible_path = []
    if col != 0 and maze[row][col-1] == 1:
        possible_path.append((row, col-1))
    if col != m-1 and maze[row][col+1] == 1:
        possible_path.append((row, col+1))
    if row != 0 and maze[row-1][col] == 1:
        possible_path.append((row-1, col))
    if row != n-1 and maze[row+1][col] == 1:
        possible_path.append((row+1, col))
    
    return possible_path

def find_path():
    visited = []
    current_layer = []
    current_layer.append([(0, 0)])
    visited.append((0, 0))
    path_len = 1
    while len(current_layer):
        current_layer.append([])
        for pos in current_layer[path_len-1]:
            for next in find_road(pos[0], pos[1]):
                if next == (n-1, m-1):
                    return path_len+1
                if next not in visited:
                    visited.append(next)
                    current_layer[path_len].append(next)
        # pos = current_layer.pop(0)
        
        path_len += 1


print(find_path())