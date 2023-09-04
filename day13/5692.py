import sys
def input():
    return sys.stdin.readline().rstrip()
while 1:
    a = input()
    if a=='0':
        break
    x=[1]
    for i in range(len(a)-1):
        x.append(x[i]*(i+2))
    for j in range(len(a)):
        x[j]*=int(a[-(j+1)])
    print(sum(x))