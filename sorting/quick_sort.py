import sys

n = int(sys.stdin.readline().strip())
numbers = list()

for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    i = start + 1
    j = end
    while i <= j:
        #print(1)
        while array[i] < array[pivot] and i < end:
            print(2)
            i += 1
        while array[j] > array[pivot] and j > start:
            print(3)
            j -= 1
        if i > j:
            tmp = array[j]
            array[j] = array[pivot]
            array[pivot] = tmp
        else:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    quick_sort(array, start, j-1)
    quick_sort(array, j+1, end)


quick_sort(numbers, 0, n-1)
print(numbers)