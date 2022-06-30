import sys

t = int(sys.stdin.readline().strip())
dp = [[0, 0] for _ in range(41)]


def arraySum(arr1, arr2):
    arr_sum = []
    arr_sum.append(arr1[0] + arr2[0])
    arr_sum.append(arr1[1] + arr2[1])
    return arr_sum


def fibonacci(n):
    if n == 1:
        return [0, 1]
    elif n == 0:
        return [1, 0]
    elif dp[n] != [0, 0]:
        return dp[n]
    else:
        dp[n] = arraySum(fibonacci(n-1), fibonacci(n-2))
        return dp[n]


for _ in range(t):
    num = int(sys.stdin.readline().strip())
    print(" ".join(map(str, fibonacci(num))))

