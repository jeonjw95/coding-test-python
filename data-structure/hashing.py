import sys

n = sys.stdin.readline().strip()
keys = sys.stdin.readline().strip()

hash_value = 0
for i, key in enumerate(keys):
    hash_value += (ord(key)-96) * 31**i

hash_value %= 1234567891

print(hash_value)
