cnt = 0

with open("070.vcf", 'r') as fr:
     for line in fr:
	if line.startswith("#"):
            pass
        else:
            l = line.split(" ")
            filt = l[6]
            if filt == "PASS":
                cnt += 1
print(cnt)



# 

