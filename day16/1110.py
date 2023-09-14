import sys
def input():
    return sys.stdin.readline().rstrip()
def cyc(a,b):    
    c = str(eval(f'{a}+{b}'))[-1]
    return b,c
n=input()
if len(n)==1:
    n ='0'+n
a,b = n[0],n[1]
cnt = 1
while 1:
    a,b = cyc(a,b)  
    if a+b==n:
        break
    else:          
        cnt+=1    
print(cnt)