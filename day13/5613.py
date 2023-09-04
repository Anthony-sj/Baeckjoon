import sys
def input():
    return sys.stdin.readline().rstrip()
x = ''
i = 0
while 1:
    a = input()
    if a == '=':
        break
    x+=a
    if i>1 and i%2==0:
        x = str(int(eval(x)))
    i+=1
print(x)