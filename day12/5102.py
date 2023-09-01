import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a, b = map(int, input().split())
    if a==b==0:
        break
    x = a-b
    print(x//2 if x%2==0 else (x-3)//2+(x<3), (x>=3)*(x%2==1))

# while(s:=input())!="0 0":a,b=map(int,s.split());q,r=divmod(a-b,2);print(max(0,q-r),[0,r][q>0])