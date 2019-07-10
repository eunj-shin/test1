# 수업 gc 함량

def calcGC(s):
    num_c = s.count('G')
    num_g = s.count('C')
    gc = (num_c + num_g)/len(s) * 100
    return gc


if __name__ == "__main__": 
    # import할 때 실행되지 않게 함
    # 밖에서 파이썬 실행할 때만 실행됨

    s = ""
    with open('sequence.txt', 'r') as fr:
        for line in fr:
            s += line.strip()
    print(s)
    gc = calcGC(s)
    print(gc)





