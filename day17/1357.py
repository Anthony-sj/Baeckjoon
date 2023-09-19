import sys
def input():
    return sys.stdin.readline().rstrip()
def Rev(X):
    while len(X)>1:
        if X[-1]!='0':
            break
        else:
            X=X[:-1]
    return int(X[::-1])
a, b = input().split()
print(Rev(str(Rev(a)+Rev(b))))