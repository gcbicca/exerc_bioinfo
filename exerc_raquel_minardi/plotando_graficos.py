""" Mapas de distância: são matrizes quadradas em que a sequencia de uma proteina é
representada nos eixos x e y e que o valor da celula (x,y) é a distancia entre os
residuos x e y na proteina."""
from math import sqrt
import plotly.express as px
import pandas

def le_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        f.close()
        return linhas


def imprime_arquivo(linhas):
    for l in linhas:  # posso iterar sobre todas as linhas do arquivo
        l = l.rstrip('\n')  # de cada linha removo a quebra de linha na direita
        print(l)  # imprimo cada linha uma abaixo da outraaaa


def obtem_cadeia(cadeia, linhas):
    atoms = {}
    for l in linhas:
        l = l.strip('\n')
        if l[0:4] == 'ATOM' and l[21] == cadeia and l[13:15] == 'CA':  #21 chainID
            res_seq = int(l[22:26])  # -> A 1  numero do residuo da sequencia
            # 31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
            x = float(l[30:38])
            # 39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
            y = float(l[38:46])
            # 47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
            z = float(l[47:54])
            atoms[res_seq] = (x, y, z)
    return atoms


def distancia(p1, p2):
    x = 0
    y = 1
    z = 2
    return sqrt((p1[x] - p2[x]) ** 2 + (p1[y] - p2[y]) ** 2 + (p1[z] - p2[z]) ** 2)


def mapa_distancia(atomos):
    matriz = []
    i = 0
    for atomos1 in atomos:
        matriz.append([])
        for atomos2 in atomos:
            matriz[i].append(distancia(atomos[atomos1], atomos[atomos2]))
        i += 1
    return matriz


# PROGRAMA PRINCIPAL
linhas = le_arquivo('1a6m.pdb')
cadeia = obtem_cadeia("A", linhas)
mapa = mapa_distancia(cadeia)
#imprime_arquivo(linhas)
print(cadeia)
#print(mapa)
fig = px.imshow(mapa)
fig.show()