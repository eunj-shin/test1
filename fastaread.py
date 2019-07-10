''''

f = "059.fasta"

with open("059.fasta", 'r') as fr:
    for line in fr:
        cnt = fr.count()

    print(cnt)
'''


# 수업
# 명령어 dd - 오려내기
# 명령어 p - 붙이기
# 명령어 yy - 한줄 카피


def fastaToString(f):
    seq = ""
    with open(f, 'r') as fr:
        for line in fr:
            if line.startswith(">"):
                pass
            else:
                seq += line.strip()
    return seq




f = "059.fasta"
seq = fastaToString(f)
print(len(seq))
print("A", seq.count("A"))
print("T", seq.count("T"))
print("G", seq.count("G"))
print("C", seq.count("C"))
