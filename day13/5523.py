import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
A,B = 0,n
for _ in range(n):
    a, b = map(int,input().split())
    A+=(a>b)
    B-=(a==b)
print(A,B-A)