import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    input()
    n,m=map(int, input().split())
    s = map(int, input().split())
    b = map(int, input().split())
    if max(s)>=max(b):
        print('S')
    else:
        print('B')