cnt = 0
seq = ""

with open("061.fastq", 'r') as fr:
    for line in fr:
        if cnt % 4 == 0: #header
            pass
        elif cnt % 4 == 1: #seq
            seq += line.strip()
        elif cnt % 4 == 2: #+
            pass
        elif cnt % 4 == 3: # qua1
            pass
        cnt += 1 # for 문 돌 때마다 하나씩 올라감:

print("num of reads:", cnt / 4)
print("length of seq:", len(seq))
