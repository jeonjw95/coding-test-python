# 복잡도: O(directions)

n = int(input())
directions = list(input().split(" "))

position = [1, 1];

for direction in directions:
    if direction == "U" and position[0] != 1:
        position[0]-= 1
    elif direction == "D" and position[0] != n:
        position[0] += 1
    elif direction == "L" and position[1] != 1:
        position[1] -= 1
    elif direction == "R" and position[1] != n:
        position[1] += 1

print(position)
