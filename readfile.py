f = "test.txt"

with open(f, 'r') as fr:
    for lines in fr:
        print(lines.strip(),end = " ")
