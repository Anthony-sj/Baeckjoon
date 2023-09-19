import sys
def input():
    return sys.stdin.readline().rstrip()
if __name__=='__main__':
    n = int(input())
    a = [True]*n
    b = list(map(int,input().split()))
    for i in range(n):
        