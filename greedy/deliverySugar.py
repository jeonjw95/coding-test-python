# 복잡도 O(N)

n = int(input())

maxFive = n // 5
isExist = False
for i in range(maxFive, -1, -1):
    currentN = n - i * 5
    if  currentN % 3 == 0:
        threeKg = currentN // 3
        fiveKg = i
        isExist = True
        break

if isExist:
    print(fiveKg + threeKg)
else:
    print(-1)

# 먼저 5로 나눌 수 있는 최대로 나누기
# 최대수 만큼 for문을 돌려서 n == 0을 만드는 최소의 3값을 찾는다. 만약 존재하지 않으면 return -1