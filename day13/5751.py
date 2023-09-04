import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a = int(input())
    if a==0:
        break
    b=sum(list(map(int,input().split())))
    print(f'Mary won {a-b} times and John won {b} times')