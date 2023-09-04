import sys
def input():
    return sys.stdin.readline().rstrip()
n=0
while 1:
    n+=1
    s = int(input())
    if s ==0:
        break
    s*=1.5/2
    s = int(s//(1.86*10**6)+(s%(1.86*10**6)>0))
    print(f"File #{n}")
    print(f"John needs {s} floppies.")
    print()