import sys

n = int(sys.stdin.readline().strip())
numbers = []


for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))


for i in range(n):
    min_num = numbers[i]
    min_index = i
    for j in range(i+1, n):
        if min_num > numbers[j]:
            min_num = numbers[j]
            min_index = j
    tmp = numbers[i]
    numbers[i] = min_num
    numbers[min_index] = tmp

for i in numbers:
    print(i)