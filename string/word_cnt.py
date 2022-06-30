import sys

word = list(sys.stdin.readline().strip().split(' '))
if word[0] == '':
    word.pop(0)
print(len(word))