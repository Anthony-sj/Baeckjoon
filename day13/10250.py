import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    h,w,n = map(int, input().split())
    x = str((n-1)%h+1)
    y = str((n-1)//h+1)
    print(x+'0'*(len(y)==1)+y)