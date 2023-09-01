import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a, b, c = map(int, input().split())
    if a==b==c==0:
        break
    x = (c-a)//b +1
    print(x if x>0 and (c-a)%b==0 else 'X')
