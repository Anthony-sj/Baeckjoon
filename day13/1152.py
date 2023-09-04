import sys
def input():
    return sys.stdin.readline().rstrip()
a = input().lstrip()
print(sum(map(lambda x : int(x==' ') , a))+1 if a!='' else 0)

# sentence = input()
# print(sentence.strip(' ').count(' ') + 1 if sentence != ' ' else 0)