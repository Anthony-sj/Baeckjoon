import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    try:
        n = int(input())
    except:
        break
    a = 1
    while 1:
        if int('1'*a)%n == 0:
            print(a)
            break
        a+=1    