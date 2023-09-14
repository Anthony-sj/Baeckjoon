import sys
def input():
    return sys.stdin.readline().rstrip()
def mul(a):
    x=1
    for i in a:
        x*=int(i)
    return x
n = input()
ans = 'NO'
for i in range(1,len(n)):
    a,b=n[:i],n[i:]
    if mul(a)==mul(b):
        ans='YES'
        break
print(ans)
