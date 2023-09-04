import sys
def input():
    return sys.stdin.readline().rstrip()
col = {
    'black' :'0',
    'brown':'1',
    'red':'2',
    'orange':'3',
    'yellow':'4',
    'green':'5',
    'blue':'6',
    'violet':'7',
    'grey':'8',
    'white':'9'
}
a,b,c= int(col[input()])*10,int(col[input()]),int(col[input()])
print((a+b)*10**(c))

# import sys
# def input():
#     return sys.stdin.readline().rstrip()
# col = {
#     'black' :'0',
#     'brown':'1',
#     'red':'2',
#     'orange':'3',
#     'yellow':'4',
#     'green':'5',
#     'blue':'6',
#     'violet':'7',
#     'grey':'8',
#     'white':'9'
# }
# a,b,c= input(),input(),input()
# if a == 'black':
#     if b == 'black':
#         print('0')
#     else:
#         print(col[b]+'0'*int(col[c]))
# else:
#     print(col[a]+col[b]+'0'*int(col[c]))