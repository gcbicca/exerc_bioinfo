# with open('', 'r') as f:
#     f = f.read()
data = 'AAAACCCGGT'
complementar= {
    'A': 'T',
    'G': 'C',
    'T': 'A',
    'C': 'G'
}
data_list = list(data)
fita_complementar = ''
for base in data_list:
    fita_complementar += complementar[base]
fita_complementar = fita_complementar[::-1]
print(fita_complementar)



