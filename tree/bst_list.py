import sys
sys.setrecursionlimit(10**8)

def postorder(tree, start, end):
    i = start + 1
    
    if start > end:
        return
    else:
        for n in range(i, end+1):
            if tree[start] < tree[n]:
                i = n
                break
    
    postorder(tree, start+1, i-1)
    postorder(tree, i, end)
    print(tree[start])
    

tree = []

while True:
    try:
        tree.append(int(sys.stdin.readline().strip()))
    except:
        break

postorder(tree, 0, len(tree)-1)