import sys
n = int(sys.stdin.readline().strip())

for _ in range(n):
    paren = sys.stdin.readline().strip()
    stack = []
    isVps = True
    for i in paren:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                isVps = False
                break
            else:
                stack.pop()

    if isVps and len(stack) == 0:
        print("YES")
    else:
        print("NO")

