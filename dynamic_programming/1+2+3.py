import sys

t = int(sys.stdin.readline().strip())
dp = [0 for _ in range(11)]


def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif dp[n]:
        return dp[n]
    else:
        dp[n] = count(n-1) + count(n-2) + count(n-3)
        return dp[n]


for _ in range(t):
    N = int(sys.stdin.readline().strip())
    print(str(count(N)))