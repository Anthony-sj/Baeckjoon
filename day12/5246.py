import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    y = [0]*8
    A = list(map(int, input().split()))
    for i in range(A[0]):
        y[A[2*i+2]-1]+=1
    print(max(y))