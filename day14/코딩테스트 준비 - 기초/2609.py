import sys
def input():
    return sys.stdin.readline().rstrip()
def get_s():
    m = 10000
    a = [1]*(1+m)
    s=[]
    for i in range(2,m+1):
        if a[i]==1:
            for j in range(i+1,m+1):
                if j%i==0:
                    a[j]=0
    for k in range(1,m+1):
        if a[k]==1:
            s.append(k)
    return s
s = get_s()
ans = 1
a,b = map(int, input().split())
idx = 1
while s[idx]<=min(a,b):
    if a%s[idx]==b%s[idx]==0:
        a//=s[idx]
        b//=s[idx]
        ans*=s[idx]
    else:
        idx+=1
print(ans)
print(a*b*ans)

# def gcd(a, b):
#     while b != 0:
#         r = a % b
#         a = b
#         b = r
#     return a
# a, b = map(int, input().split())
# print(gcd(a, b))
# print(a*b // gcd(a, b))