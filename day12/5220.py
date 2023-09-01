import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    a, b = map(int, input().split())
    x = 0
    while a >0:
        if a%2==1:
            x+=1
        a//=2
    print(("Valid","Corrupt")[x%2!=b])