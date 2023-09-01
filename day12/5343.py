import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    a = input()
    t = 0
    for i in range(len(a)//8):
        b = sum([int(x) for x in a[i*8:i*8+7]])
        if b%2 != int(a[8*(i+1)-1]):
            t+=1
    print(t)