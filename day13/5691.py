import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a,b = map(int,input().split())
    if a==b==0:
        break
    print((2*a)-b)