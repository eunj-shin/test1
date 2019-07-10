l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
#l = a.sort()

#print(a[-1])
#print(a[0])


for i in range(0, len(l), 1):
    if i ==0:   #set max_val, min_val
        max_val = l[i]
        min_val = l[i]
    else:
        if max_val < l[i]:
            max_val = l[i] # max_val change
        if min_val > l[i]:
            min_val = l[i] # min_val change

print("max:",max_val)
print("min:",min_val)
print("----")

# 파이썬 내장함수로도 가능
print("max:",max(l))
print("min:",min(l))
