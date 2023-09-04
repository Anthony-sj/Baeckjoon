import sys
def input():
    return sys.stdin.readline().rstrip()
n,f = int(input()[:-2]+'00'), int(input())
a = str((f - n%f)%f)
print('0'*(len(a)==1)+a)