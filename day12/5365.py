import sys
def input():
    return sys.stdin.readline().rstrip()
k = int(input())
t = input()+' '
x = 1
for _ in range(k):
    print(t[x-1] if t.find(' ')>=x else ' ',end='')
    x = t.find(' ')
    t = t[x+1:]