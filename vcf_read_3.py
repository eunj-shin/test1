'''

alts = "A,G"
alts.split(",")
['A', 'G']

alts = "C"
alts.split(",")
['C']

'''
cnt = 0

with open('070.vcf', 'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split("\t")
            ref = l[3]
            alts = l[4].split(",")
            for alt in alts:
                cnt += 1

print(cnt)
