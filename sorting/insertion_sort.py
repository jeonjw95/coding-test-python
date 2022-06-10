import sys

n = int(sys.stdin.readline().strip())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if numbers[j-1] > numbers[j]:
            tmp = numbers[j-1]
            numbers[j-1] = numbers[j]
            numbers[j] = tmp
        else:
            break

for n in numbers:
    print(n)
