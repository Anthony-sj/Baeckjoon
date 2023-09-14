import sys
def input():
    return sys.stdin.readline().rstrip()
def check_row(b,n,i):
    cnt = [0]
    c = 1
    r = 0
    for l in range(1,n+1):
        if b[i][l] == b[i][l+1]:
            c+=1
        else:
            cnt.append(c)
            c=1
    return max(cnt)
def check_col(b,n,j):
    cnt = [0]
    c = 1
    r = 0
    for k in range(1,n+1):
        if b[k][j] == b[k+1][j]:
            c+=1            
        else:            
            if b[k][j]==b[k+1][j+1] or b[k][j]==b[k+1][j-1]:
                c+=1
                if b[k][j]==b[k+2][]
            else:
                cnt.append(c)

                c=1                
    for k in range(n,0,-1):
        if b[k][j] == b[k-1][j]:
            c+=1
        else:
            if b[k][j]==b[k-1][j+1] or b[k][j]==b[k-1][j-1]:
                c+=1
                if b[k][j]==b[k-2][j]:
                    cnt.append(c+1)
                    c=1
                else:
                    cnt.append(c)
                    c=1
            else:
                cnt.append(c)
                c=1
    return max(cnt)
n=int(input())
b = ['#'+('#'*n if q*(n-(q-1))==0 else input())+'#' for q in range(n+2)]
max_cnt = 1
while max_cnt<n:
    for i in range(1,n+2):
        max_cnt = max(max_cnt,check_row(b,n,i))
        max_cnt = max(max_cnt,check_col(b,n,i))
    break
print(max_cnt)