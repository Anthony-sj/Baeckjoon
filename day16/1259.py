import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a = input()
    if a =='0':
        break
    print(('no','yes')[a==a[::-1]])
