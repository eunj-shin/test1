Seq1 = 'ATGTTATAG'
# print(Seq1[::-1]) 
# 다른 언어에서 사용불가- python에서만


revSeq1 = ""
for i in range(len(Seq1)-1,-1,-1):
    revSeq1 += Seq1[i]
print(revSeq1)
