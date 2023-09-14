import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = int(input()),5
studs = [list(input().split()) for _ in range(n)]
x = [0]*n
for i in range(n):
    y=[True]*n
    for j in range(m):
        a = studs[i][j]
        for k in range(n):
            if i!=k and y[k] and a==studs[k][j]:
                x[i]+=1
                y[k]=False
print(x.index(max(x))+1)