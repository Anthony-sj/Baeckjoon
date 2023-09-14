import sys
def input():
    return sys.stdin.readline().rstrip()
def get_prime():
    max = 1000000
    p = [0,0]+[1]*(max-1)
    for i in range(2,1001):
        if p[i]:
            p[i*i::i]=[0]*len(p[i*i::i])
    return p
p = get_prime()
while 1:
    n = int(input())
    if n ==0:
        break
    ans = "Goldbach's conjecture is wrong."
    for i in range(3,n//2+1,2):
        if p[i] and p[n-i]:
            ans = f"{n} = {i} + {n-i}"
            break
    print(ans)