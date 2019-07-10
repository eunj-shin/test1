Seq1 = "ATGTTATAG"
#li = Seq1.list()

newSeq1 = ""
#상보적 서열 만들기


for i in Seq1:
    if i == 'A':
        print newSeq1 += 'T'
    elif i == 'T':
        print newSeq1 += 'A'
    elif i == 'C':
        print newSeq1 += 'G'
    elif i == 'G':
        print newSeq1 += 'C'

