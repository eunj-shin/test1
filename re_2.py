base = input('Enter the one base: ')

d1 = {}
d1('A') = 'Adenine'
d1('C') = 'Cytosine'
d1('G') = 'Guanine'
d1('T') = 'Thymine'
d1('U') = 'Uracil'

print(d1.get(str(base)))
