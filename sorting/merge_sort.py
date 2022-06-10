import sys

n = int(sys.stdin.readline().strip())
numbers = list()
for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))


def merge_sort(array, start, ends):
    if start == ends:
        return [array[start]]

    middle = (start+ends) // 2
    return merge(merge_sort(array, start, middle), merge_sort(array, middle+1, ends))


def merge(a1, a2):
    merge_num = list()
    while len(a1) and len(a2):
        if a1[0] < a2[0]:
            merge_num.append(a1.pop(0))
        else:
            merge_num.append(a2.pop(0))
    merge_num += a1
    merge_num += a2

    return merge_num


numbers = merge_sort(numbers, 0, n-1)

for n in numbers:
    print(n)