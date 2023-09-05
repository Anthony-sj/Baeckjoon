import sys
def input():
    return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
for i in range(a,b+1):
    if i==1: continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)

# def get_t():
#     max = 1000
#     s = [0,0]+[1]*(max-1)
#     for i in range(2,max+1):
#         if s[i]==1:
#             for j in range(i+1,max+1):
#                 if j%i==0:
#                     s[j]=0
#     t=[]
#     for k in range(2,max+1):
#         if s[k]==1:
#             t.append(k)
#     return t
# t = get_t()
# a,b=map(int,input().split())
# for q in range(a,b+1):
#     if q == 1:continue
#     elif q <= 1000:
#         if q in t:
#             print(q)
#     else:
#         for p in t:
#             if q%p==0:
#                 break
#             else:
#                 print(q) 
