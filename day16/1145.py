import sys
def input():
    return sys.stdin.readline().rstrip()
# def get_prime():
#     max=100
#     prime = [2]
#     for i in range(3,max+1):
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 break
#         else:
#             prime.append(i)
#     return prime
# def get_sol(p,a,b,c):
#     x=1
#     idx = 0    
#     while a!=1 or b!=1 or c!=1:
#         t = p[idx]
#         if a%t==0 or b%t==0 or c%t==0:
#             x*=t
#             if a%t==0:
#                 a//=t
#             if b%t==0:
#                 b//=t
#             if c%t==0:
#                 c//=t            
#         else:
#             idx+=1
#     return x
# p = get_prime()
# nums = sorted(list(map(int, input().split())))
# min = nums[0]*nums[1]*nums[2]
# N = []
# for i in range(3):
#     for j in range(i+1,4):
#         for k in range(j+1,5):
#             N.append([nums[i],nums[j],nums[k]])
# for a,b,c in N:
#     s = get_sol(p,a,b,c)
#     if s<min:
#         min = s
# print(min)
import sys
def input():
    return sys.stdin.readline().rstrip()
nums = list(map(int, input().split()))
min_n = min(nums)
while 1:
    cnt = 0
    for i in nums:
        if min_n%i==0:
            cnt+=1
    if cnt>=3:
        break
    else:
        min_n+=1
print(min_n)
    