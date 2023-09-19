import sys
def input():
    return sys.stdin.readline().rstrip()
def m(a):
    M = max(a)
    for i in range(len(a)):
        a[i]=(a[i]/M)*100
    return sum(a)
if __name__=='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(m(a)/n)
