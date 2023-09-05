import sys
def input():
    return sys.stdin.readline().rstrip('')
def get_a():
    m = 1000
    a = [0,0]+[1]*(m-1)
    for i in range(2,m+1):
        if a[i]==1:
            for j in range(i+1,m+1):
                if j%i==0:
                    a[j]=0    
    return a
a=get_a()
n=int(input())
t=map(int,input().split())
print(sum([a[i] for i in t]))
