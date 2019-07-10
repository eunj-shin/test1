with open('test.txt', 'r') as fr:
    for line in fr:  #메모리 소모 없이 한줄씩 읽을 수 있음
        print(line.strip())

#ctrl + v + tab -> tab이 들어감
