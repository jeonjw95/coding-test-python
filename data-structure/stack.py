import sys

stack = []


def push(x):
    stack.append(int(x))


def pop():
    if len(stack):
        return stack.pop()
    else:
        return -1


def size():
    return len(stack)


def empty():
    if not len(stack):
        return 1
    else:
        return 0


def top():
    if empty():
        return -1
    else:
        return stack[-1]


n = int(sys.stdin.readline().strip())

for i in range(n):
    command = sys.stdin.readline().strip()
    word = command.split()
    func = word[0]

    if func == "push":
        push(word[1])
    elif func == "pop":
        print(pop())
    elif func == "size":
        print(size())
    elif func == "empty":
        print(empty())
    elif func == "top":
        print(top())

