with open("re2_3.text", 'r') as fr:
    header = fr.readline().strip().split(",")
    val = fr.readline().strip().split(",")

d = {}
for i in range(len(header)):
    k = header[i]
    v = val[i]
    d[k] = v

print(d)
