import sys

expr = sys.stdin.readline().strip()
stack = []
postfix = []


def is_operator(ele):
    if ele == '(' or ele == ')' or ele == '*' or ele == '/' or ele == '+' or ele == '-':
        return True
    else:
        return False


def priority(oper):
    if oper == '*' or oper == '/':
        return 2
    elif oper == '+' or oper == '-':
        return 1


def compare(a, b):
    if a > b:
        return 1
    else:
        return 0


def iterate_compare(oper):
    if len(stack) == 0:
        stack.append(oper)
        return

    while len(stack) and stack[-1] != '(' and not compare(priority(oper), priority(stack[-1])):
        postfix.append(stack.pop())
    stack.append(oper)


for i in expr:
    if i == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()
    elif i == '(':
        stack.append(i)
    elif is_operator(i):
        iterate_compare(i)
    else:
        postfix.append(i)

while len(stack):
    postfix.append(stack.pop())

print("".join(postfix))
