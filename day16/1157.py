import sys
def input():
    return sys.stdin.readline().rstrip()
S = input().upper()
idxs = [0]*26
for s in S:
    idxs[ord(s)-ord('A')]+=1
if idxs.count(max(idxs))>=2:
    print('?')
else:
    print(chr(ord('A')+idxs.index(max(idxs))))