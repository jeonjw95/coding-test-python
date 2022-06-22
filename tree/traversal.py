import sys
from collections import defaultdict

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        

def preorder(root):
    print(root.data, end='')
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
        
        
def postorder(root):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.data, end='')
    

def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.data, end='')
    if root.right:
        inorder(root.right)
        
        
def factory():
    return None

nodes = defaultdict(factory)

n = int(sys.stdin.readline().strip())

for _ in range(n):
    data, left, right = sys.stdin.readline().strip().split(' ')
    data_node = nodes[data]
    left_node = nodes[left]
    right_node = nodes[right]
    
    if left == '.':
        left = None
    if right == '.':
        right = None
    
    if left is not None and left_node is None:
        nodes[left] = Node(left, None, None)
        left_node = nodes[left]
    if right is not None and right_node is None:
        nodes[right] = Node(right, None, None)
        right_node = nodes[right]
    if data_node is None:
        nodes[data] = Node(data, left_node, right_node)
    else:
        nodes[data].left = left_node
        nodes[data].right = right_node

        
root = nodes['A']

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()