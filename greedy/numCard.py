# 복잡도 O(row)

row, col = map(int, input().split(" "))
cards = []
max_num = 0
for i in range(row):
    cards.append(list(map(int, input().split(' '))))
    max_num = max(max_num, min(cards[i]))

print(max_num)