import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    try:
        h, p = map(int, input().split())
    except:
        break
    print(f'{h/p:.2f}')