import sys
def input():
    return sys.stdin.readline().rstrip()
def get_score(S):
    d={'L':0,'O':0,'V':0,'E':0}
    for s in S:
        if s in 'LOVE':
            d[s]+=1
    L,O,V,E = (d[i] for i in 'LOVE')    
    return ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
a = input()
B = sorted([input() for _ in range(int(input()))])
y = []
for b in B:
    y.append(get_score(a+b))
print(B[y.index(max(y))])