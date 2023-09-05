import sys
def input():
    return sys.stdin.readline().rstrip()
n=int(input())
print(sum(k*(n//k)for k in range(1,n+1)))