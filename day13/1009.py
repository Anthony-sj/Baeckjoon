import sys
def input():
    return sys.stdin.readline().rstrip()
T = [10,1,2,3,4,5,6,7,8,9]
x = 0
s = int(input())
while x<s:
    a, b = map(int, input().split())
    b = b%4 + 4*(b%4==0)
    a = str(a**(b))[-1]
    print(T[int(a)])
    x+=1