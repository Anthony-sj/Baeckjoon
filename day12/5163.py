import sys, math
def input():
    return sys.stdin.readline().rstrip()
pi = math.pi
for i in range(int(input())):
    b,w = map(float, input().split())
    for _ in range(int(b)):
        r = float(input())
        w -= pi*r*r*r/750
    print(f'Data Set {i+1}:')
    print(('Yes','No')[w>=0], end='\n\n')