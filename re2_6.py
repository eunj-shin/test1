import sys

def kmer(l1, l2, n):
    if n==1:
         return l2

     ltmp = [] # new result
     for s1 in l1:
         for s2 in l2:
             ltmp.append(s1+s2)
     print(n, ltmp)
     return kmer(l1, ltmp, n-1)

 n = int(sys.argv[1])
 l1 = ["A", "C", "G", "T"] # template
 l2 = ["A", "C", "G", "T"] # result

result = kmer(l1, l2, n)
print(result)
