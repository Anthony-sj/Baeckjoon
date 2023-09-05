import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
print(max(a)*min(a))