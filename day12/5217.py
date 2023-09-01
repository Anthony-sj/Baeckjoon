import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n = int(input())
    y=[]
    for i in range(1,12):
        for j in range(i+1,13):
            if i+j>n:
                break
            elif i+j==n:
                y.append(' '.join([str(i),str(j)]))
    print(f'Pairs for {n}: '+ ', '.join(y))
