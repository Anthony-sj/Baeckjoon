import sys
def input():
    return sys.stdin.readline().rstrip()
if __name__=='__main__':
    # d = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
    #    "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
    #    "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}
    # n=int(input())
    # seq=input()
    # a=seq[-1]
    # for s in seq[:-1][::-1]:
    #     a = d[s+a]
    # print(a)
    dna = 'ACAGCGTAATCGGAGT'
    d = {'A':0,'G':1,'C':2,'T':3}
    n=int(input())
    seq=input()
    a=seq[-1]
    for s in seq[:-1][::-1]:
        a=dna[d[s]*4+d[a]]
    print(a)

        

    
    