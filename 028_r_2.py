Seq1 = 'ATGTTATAG'
compSeq = ""
compDic = {
        "A":"T", 
        "C":"G", 
        "G":"C", 
        "T":"A"
        }

for s in Seq1:
    compSeq += compDic[s]

print(Seq1)
print(compSeq)
