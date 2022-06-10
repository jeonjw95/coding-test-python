import sys

n = int(sys.stdin.readline().strip())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            tmp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = tmp

for n in numbers:
    print(n)

