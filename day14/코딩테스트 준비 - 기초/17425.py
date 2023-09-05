import sys
def input():
    return sys.stdin.readline().rstrip()
def get_g():
    m=1000000
    dp=[1]*(m+1)
    a=[0]*(m+1)
    for i in range(2,m+1):
        j=1
        while i*j<=m:
            dp[i*j]+=i
            j+=1
    for k in range(1,m+1):
        a[k]=a[k-1]+dp[k]
    return a
a = get_g()
for _ in range(int(input())):
    n=int(input())        
    print(a[n],end='\n')