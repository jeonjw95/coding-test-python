import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    
def push(root, node):
    if node.data < root.data:
        if root.left == None:
            root.left = node
        else:
            push(root.left, node)
    elif root.data < node.data:
        if root.right == None:
            root.right = node
        else:
            push(root.right, node)

def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.data)
            
root = None

while True:
    try:
        node = Node(int(sys.stdin.readline().strip()), None, None)
        if root is None:
            root = node
        else:
            push(root, node)
    except:
        break

postorder(root)