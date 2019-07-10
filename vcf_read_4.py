snp_num = 0
ins_num = 0
del

with open("070.vcf", 'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            l = line.split("\t")
            ref = l[3]
            alts = l[4].split(",")
            for alt in alts:
                if len(ref) == len(alt):
                    snp_num += 1
                elif len(ref) < len(alt):
                    ins_num += 1
                elif len(ref) > len(alt):
                    del_num += 1
