import sys
import kmer2

def checkPalindrome(s):
    s_rev = s[::-1]
    if s == s_rev:
        return True
    else:
        return False

if len(sys.argv) !=2:
    print("#usage: python %s [number]" % sys.argv[0])
    sys.exit()

n = int(sys.argv[1]_
l1 = ["A", "C", "G", "T"]
l2 = ["A", "C", "G", "T"]
result = kmer2.kmer(l1,l2,n)

cnt = 0


