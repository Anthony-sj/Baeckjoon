import sys
def input():
    return sys.stdin.readline().rstrip()
h,m,s = map(int,input().split())
y = h*3600 + m*60 + s
for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0]==3:

        print((y//3600)%24,(y//60)%60,y%60)
    else:
        if q[0] == 1:
            y += q[1]
        elif q[0] == 2:
            y -= q[1]