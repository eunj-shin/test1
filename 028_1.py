Seq1="ATGTTATAG"
list_blank=[]
for txt in Seq1:
    if txt == 'A':
        txt = 'T'
    elif txt == 'T':
        txt = 'A'
    elif txt == 'C':
        txt = 'G'
    elif txt == 'G':
        txt = 'C'
    list_blank.append(txt)
print (''.join(list_blank))
