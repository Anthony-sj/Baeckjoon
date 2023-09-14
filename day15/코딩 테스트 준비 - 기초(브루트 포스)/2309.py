import sys
def input():
    return sys.stdin.readline().rstrip()
a = []
for _ in range(9):
    a.append(int(input()))
a=sorted(a)
n=sum(a)-100
m=0
while a[m]<n//2+1:
    if n-a[m] in a:
        a.remove(n-a[m])
        a.remove(a[m])        
        break
    m+=1
print('\n'.join(map(str,a)))