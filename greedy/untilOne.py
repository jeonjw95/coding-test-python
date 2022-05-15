n, k = map(int, input().split(" "))
cnt = 0

while True:
    cnt += n - n//k*k
    n //= k
    cnt += 1
    if n < k:
        break
cnt += n-1
print(cnt)