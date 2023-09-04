import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    print(' '*(n-i-1),end='')
    if i == 0 or i==n-1:
        print('*'*(2*i+1))
    else:
        print('*'+' '*(2*i-1)+'*')
