import sys
def input():
    return sys.stdin.readline().rstrip()
a,b = 0,0
for _ in range(int(input())):
    x,y=map(int, input().split())
    if x>y:
        a+=x+y
    elif x<y:
        b+=x+y
    else:
        a+=x;b+=x
print(a,b)