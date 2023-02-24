with open('rosalind_revc.txt', 'r') as f:
    f = f.read()
    complementar= {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }

    def complementor(x):
        return complementar[x]


    r = list(map(complementor, f[::-1].strip()))
    r = ''.join(r)
    print(r)