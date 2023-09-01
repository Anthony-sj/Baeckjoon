import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    A = list(map(int, input().split()))[1:]
    B = [b if b%2==0 else 0 for b in A]
    x = sum(B)/sum(A)
    print(('ODD','TIE','EVEN')[(x>=0.5)+(x>0.5)])
