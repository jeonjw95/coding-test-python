import sys
from collections import defaultdict

# 트리의 레벨을 각 노드 마다 부여한 후 짝수 계층의 노드 수와 홀수 계층의 노드 수 중 작은 수를 선택

# 

# n = int(sys.stdin.readline().strip())

# def bfs(root):
#     visited = [root]
#     layers = [[root]]
#     current = 0
    
#     while len(layers[current]):
#         layers.append([])
#         for next in layers[current]:
#             for child in graph[next]:
#                 if child not in visited:
#                     visited.append(child)
#                     layers[current+1].append(child)
#         current += 1
    
#     even = 0    #짝수
#     odd = 0     #홀수

#     for i, layer in enumerate(layers):
#         if i % 2 == 0:
#             even += len(layer)
#         else:
#             odd += len(layer)
    
#     print("even:" + str(even))
#     print('odd:' + str(odd))
#     if even >= odd:
#         return odd
#     else:
#         return even

graph = defaultdict(list)

for _ in range(n-1):
    node1, node2 = map(int, sys.stdin.readline().strip().split(' '))
    graph[node1].append(node2)
    graph[node2].append(node1)

# min_nums = []
# for i in range(1, n+1):
#     min_nums.append(bfs(i))

# print(min(min_nums))