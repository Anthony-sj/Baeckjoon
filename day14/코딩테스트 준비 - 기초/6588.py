import sys
def input():
    return sys.stdin.readline().rstrip()
def get_s():
    max = 1000000
    s = [0,0,0]+[1]*(max-2)
    for i in range(3,max+1):
        if s[i]==1:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    s[i]=0
                    break
    return s
s=get_s()
while 1:
    n = int(input())
    ans = "Goldbach's conjecture is wrong."
    m = 3
    while m<n/2:
        if s[n-m] == 1:
            if s[m] == 1:
                ans=(f'{n} = {m} + {n-m}')
                break
        m+=2
    print(ans)