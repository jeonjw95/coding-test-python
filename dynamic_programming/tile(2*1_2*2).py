import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline().strip())

dp = [0] * (n + 1)


def find_tile(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    if dp[x] != 0:
        return dp[x]
    dp[x] = find_tile(x-1) + 2 * find_tile(x-2)
    return dp[x]


print(find_tile(n) % 10007)

