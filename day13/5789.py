import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    a = input()
    x = len(a)//2
    print('Do-it'+'-Not'*(a[x]!=a[x-1]))