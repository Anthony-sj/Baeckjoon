import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    n,d = map(int, input().split())
    if n==d==0:
        break
    a = list(map(int, input().split()))
    for _ in range(d-1):
        b = list(map(int, input().split()))
        for i in range(n):
            a[i]+=b[i]
    print(('no','yes')[max(a)==d])