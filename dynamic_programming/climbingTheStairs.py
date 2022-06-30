import sys

n = int(sys.stdin.readline().strip())
stairs = [0]
dp = [[0, 0] for _ in range(n+1)] # dp[n][0] == n-2, dp[n][1] == n-1

for _ in range(n):
    score = int(sys.stdin.readline().strip())
    stairs.append(score)


def find_child(n, p):
    child = []
    if p-n == 1 and n != 2:
        child.append(n-2)
    else:
        child.append(n-2, n-1)

    return child


def find(n, p):     #p = parents
    if n == 0:
        return 0
    elif n == 1:
        return stairs[1]
    elif p-n == 1:
        if dp[n][0] != 0:
            return dp[n][0]
        else:
            dp[n][0] = stairs[n] + find(n-2, n)
            return dp[n][0]
    elif p-n != 1:
        if dp[n][0] == 0:
            dp[n][0] = stairs[n] + find(n - 2, n)
        if dp[n][1] == 0:
            dp[n][1] = stairs[n] + find(n - 1, n)
        return max(dp[n][0], dp[n][1])


print(str(find(n, -2)))