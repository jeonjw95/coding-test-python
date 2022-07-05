# visited = {}
#
# for a in range(64, 90):
#     alpha = chr(a + 1)
#     visited[alpha] = 0
#
# print(visited)

visited = [0] * 26
visited[0] = 1
visited[2] = 1

print(visited[ord('C') - 65])