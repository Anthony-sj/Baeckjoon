import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a = int(input())
    if a==0:
        break
    x = [i*i for i in range(1,a+1)]
    print(sum(x))