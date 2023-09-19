import sys
def input():
    return sys.stdin.readline().rstrip()
def fibo(m):
    x = [1]+[m[i]+m[i+1] for i in range(len(m)-1)]+[1]
    return x
def get_result(a,m):
    x=0
    for i in range(len(a)):
        x+=a[i]*m[i]*((-1)**(i))
    return x
if __name__=='__main__':
    y = []
    n,k = map(int, input().split())
    a = list(map(int, input().split(',')))    
    if k!=0:
        m=[1]
        while len(m)-1<k:
            m = fibo(m)
        for j in range(n-k):
            y.append(str(get_result(a[j:j+len(m)][::-1],m)))
        print(','.join(y))
    else:
        print(','.join(map(str, a)))