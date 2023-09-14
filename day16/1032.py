import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
x = [c for c in input()]
for _ in range(n-1):
    y = input()
    for i in range(len(x)):
        if x[i]!=y[i]:
            x[i]='?'
print(''.join(x))