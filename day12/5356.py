import sys
def input():
    return sys.stdin.readline().rstrip()
for _ in range(int(input())):
    a, b = input().split()
    for i in range(int(a)):
        x = ord(b)+i
        print(chr((x-26*(x>ord('Z'))))*(i+1))
    print()