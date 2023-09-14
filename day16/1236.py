import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = map(int, input().split())
x,y = [True]*n,[True]*m
for i in range(n):
    t = input()
    for j in range(m):
        if t[j]=='X':
            x[i]=False
            y[j]=False
print(max(sum(x),sum(y)))