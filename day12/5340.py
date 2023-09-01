import sys
def input():
    return sys.stdin.readline().rstrip()
x=[]
for _ in range(6):
    x.append(str(len(input())))
print(f"Latitude {':'.join(x[:3])}")
print(f"Longitude {':'.join(x[3:])}")