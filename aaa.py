import sys
def input():
    return sys.stdin.readline().rstrip()
T = ('Scalene','Isosceles','Equilateral','Invalid')
while 1:
    x = -1
    a,b,c = sorted(map(int,input().split()))
    if a==b==c==0:
        break
    if c<a+b:
        x+=1
        if a==b or b==c:
            x+=1
            if a==b==c:
                x+=1            
    print(T[x])