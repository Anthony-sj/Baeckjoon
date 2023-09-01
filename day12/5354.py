import sys
def input():
    return sys.stdin.readline().rstrip()
k = int(input())
for q in range(k):
    a = int(input())
    for i in range(a):
        print('#'*(a>=1)+'J#'[i==0 or i==a-1]*(a-2)*(a>2)+'#'*(a>=2))
    print()