import sys
def input():
    return sys.stdin.readline().rstrip()
a,b = map(int, input().split())
x=[]
i=1
while len(x)<b:
    x+=[i]*i
    i+=1
print(sum(x[a-1:b]))