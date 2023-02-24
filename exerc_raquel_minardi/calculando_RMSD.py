""" VAMOS FAZER A COMPARACAÇÃO COM PROTEINAS IDENTICAS MAS COM CONFORMAÇÕES DIFERENTES"""
from math import sqrt

def le_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        f.close()
        return linhas


def imprime_arquivo(linhas):
    for l in linhas:  # posso iterar sobre todas as linhas do arquivo
        l = l.rstrip('\n')  # de cada linha removo a quebra de linha na direita
        print(l)  # imprimo cada linha uma abaixo da outra

def obtem_modelo(num, linhas):
    atoms = {}
    for l in linhas:
        l = l.strip('\n')
        if l[0:5] == 'MODEL':
            modelo = int(l[10:14])
        elif l[0:4] == 'ATOM' and modelo == num:
        #  7 - 11        Integer       serial       Atom  serial number.
            serial = int(l[6:11])
        # 31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
            x = float(l[30:38])
        # 39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
            y = float(l[38:46])
        # 47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
            z = float(l[46:54])
            atoms[serial] = (x,y,z)
    return atoms


def rmsd(proteina1, proteina2):
    x = 0
    y = 1
    z = 2
    soma = 0
    for i in proteina1.keys():
        soma += (proteina1[i][x] - proteina2[i][x])**2 + (proteina1[i][y] - proteina2[i][y])**2 + (proteina1[i][z] - proteina2[i][z])**2
    n = len(proteina1)  # as duas proteinas tem o mesmo tamanho
    return sqrt(soma/n)



# PROGRAMA PRINCIPAL
linhas = le_arquivo('2m6q.pdb')
#imprime_arquivo(linhas)
#print(obtem_modelo(1,linhas))
mod1 = obtem_modelo(1, linhas)
mod2 = obtem_modelo(5, linhas)
print(rmsd(mod1, mod2))