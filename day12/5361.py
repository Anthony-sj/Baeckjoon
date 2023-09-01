import sys
def input():
    return sys.stdin.readline().rstrip()
T = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(int(input())):
    A = list(map(int, input().split()))
    x = 0
    for i in range(5):
        x+= A[i]*T[i]
    print(f'${x:.2f}')