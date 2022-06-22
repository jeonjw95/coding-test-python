import sys

n = int(sys.stdin.readline().strip())
apt = []

for _ in range(n):
    apt.append(list(map(int, list(sys.stdin.readline().strip()))))
    

    
def find_adjacency(row, col):
    adjacency = []
    if row !=0 and apt[row-1][col] == 1:
        adjacency.append((row-1, col))
    if row != n-1 and apt[row+1][col] == 1:
        adjacency.append((row+1, col))
    if col != 0 and apt[row][col-1] == 1:
        adjacency.append((row, col-1))
    if col != n-1 and apt[row][col+1] == 1:
        adjacency.append((row, col+1))
    
    return adjacency

def find_complex(row, col):
    complex = [(row, col)]
    layer = [[(row, col)]]
    current = 0
    
    while len(layer[current]):
        layer.append([])
        for pos in layer[current]:
            for next in find_adjacency(pos[0], pos[1]):
                if next not in complex:
                    complex.append(next)
                    layer[current+1].append(next)
        current += 1
        
    return complex


def find_complex_number():
    visited = []
    complexes = []
    
    for i, row in enumerate(apt):
        for j, col in enumerate(row):
            if col == 1 and (i, j) not in visited:
                complex = find_complex(i, j)
                visited += complex
                complexes.append(complex)
                
    return complexes
    
complexes_num = find_complex_number()
print(len(complexes_num))
sorted_num = []
for i in complexes_num:
    sorted_num.append(len(i))
sorted_num.sort()

for i in sorted_num:
    print(i)
