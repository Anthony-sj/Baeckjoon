import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
while 1:
    x=1
    for i in str(n):
        if i!='4' and i!='7':
            x=0
            n-=1
    if x==1:
        print(n)
        break