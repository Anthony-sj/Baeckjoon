import sys
def input():
    return sys.stdin.readline().rstrip()
for i in range(1, int(input())+1):
    if i%3==0 or i%5==0:
        print('Dead'*(i%3==0)+'Man'*(i%5==0), end='\n')
    else:
        print(i, end=' ')