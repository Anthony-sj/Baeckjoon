import sys
def input():
    return sys.stdin.readline().rstrip()
a = int(input())
for _ in range(9):
    a-=int(input())
print(a)