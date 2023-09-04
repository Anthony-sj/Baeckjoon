import sys
def input():
    return sys.stdin.readline().rstrip()
x = 0
for i in range(8):
    a = input()
    for j in [0,2,4,6]:
        x+=('F' == a[j+i%2])
print(x)