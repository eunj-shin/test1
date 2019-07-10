Seq1 = 'AGTTTATAG'


for i in range(0,len(Seq1),1):
    if Seq1[i:i+2] == 'TT':
        print(i, "-->", i, ":", i+2, Seq1[i:i+2])



#Seq1.index('TT')

#for i in range(0, len(Seq1)-1):
#    i = 'TT'
#    print (Seq1.index('TT'))
