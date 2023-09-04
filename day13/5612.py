import sys
def input():
    return sys.stdin.readline().rstrip()
n,m = int(input()), [int(input())]
for i in range(n):
    a,b = map(int, input().split())
    m.append(m[i]+a-b)
print((max(m),0)[0 > min(m)])