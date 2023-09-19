import sys
def input():
    return sys.stdin.readline().rstrip()
x = input()
a = int(x,2)
print(oct(a)[2:])
# if len(x)%3!=0:
#     x = '0'*(3-(len(x)%3))+x
# r = []
# for i in range(len(x)//3):
#     r.append(str(4*(x[3*i]=='1')+2*(x[3*i+1]=='1')+(x[3*i+2]=='1')))
# print(''.join(r))
