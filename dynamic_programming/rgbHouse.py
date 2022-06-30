import sys

sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())
house = [[0, 0, 0] for _ in range(1001)]
dp = [[-1, -1, -1] for _ in range(1001)]

def findMinCost(n, p):
    rgb = [0, 1, 2]
    rgb.remove(p)
    if n == 1:
        for color in rgb:
            dp[1][color] = house[1][color]
        return
    else:
        for color in rgb:
            minCost = 1000001
            nextColor = [0, 1, 2]
            nextColor.remove(color)
            for next in nextColor:
                if dp[n - 1][next] != -1:
                    minCost = min(minCost, dp[n - 1][next])
                else:
                    findMinCost(n - 1, color)
                    minCost = min(minCost, dp[n - 1][next])
            dp[n][color] = house[n][color] + minCost

    minCost = 1000001
    for i in rgb:
        minCost = min(minCost, dp[n][i])

    return minCost


for i in range(1, N+1):
    r, g, b = map(int, sys.stdin.readline().strip().split(' '))
    house[i][0] = r
    house[i][1] = g
    house[i][2] = b


red = findMinCost(N, 0)
green = findMinCost(N, 1)
blue = findMinCost(N, 2)

print(min(red, green, blue))