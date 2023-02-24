import math
def le_arquivo(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        f.close()
        return linhas


def imprime_arquivo(linhas):
    for l in linhas:  # posso iterar sobre todas as linhas do arquivo
        l = l.rstrip('\n')  # de cada linha removo a quebra de linha na direita
        print(l)  # imprimo cada linha uma abaixo da outra


def obtem_cadeia(linhas, cadeia=None):
    atoms = {}
    for l in linhas:
        l = l.rstrip('\n')
        if l[0:4] == 'ATOM' and l[21] == cadeia:  # documentacao -1 (posicao 22 ->21)
            #  7 - 11        Integer       serial       Atom  serial number.
            serial = int(l[6:11])
            # 18 - 20        Residue name  resName      Residue name.
            res_name = (l[17:20])
            # 23 - 26        Integer       resSeq       Residue sequence number.
            res_seq = int(l[22:26])
            # 31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
            x = float(l[30:38])
            # 39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
            y = float(l[38:46])
            # 47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
            z = float(l[46:54])
            atoms[serial] = (x, y, z, res_name, res_seq)
    return atoms


def obtem_molecula(linhas, id=None):
    atoms = {}
    for l in linhas:
        l = l.rstrip('\n')
        if l[0:6] == 'HETATM' and l[17:20] == id:  # documentacao -1 (posicao 22 ->21)
            #  7 - 11        Integer       serial       Atom  serial number.
            serial = int(l[6:11])
            # 13 - 16       Atom           name          Atom name.
            atom_name = (l[12:16]).strip()
            # 31 - 38        Real(8.3)     x            Orthogonal coordinates for X in Angstroms.
            x = float(l[30:38])
            # 39 - 46        Real(8.3)     y            Orthogonal coordinates for Y in Angstroms.
            y = float(l[38:46])
            # 47 - 54        Real(8.3)     z            Orthogonal coordinates for Z in Angstroms.
            z = float(l[46:54])
            atoms[serial] = (x, y, z, atom_name)
    return atoms


def dist(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)



def obtem_sitio_ligacao(moleculas, cadeias, limiar):
    x = 0
    y = 1
    z = 2
    res_name = 3
    res_seq = 4
    name = 3
    sitio = []
    for molecula in moleculas:
        for aa in cadeias:
            """como pegarei cada atomo da minha moleculas"""
            d = dist(moleculas[molecula][x], moleculas[molecula][y], moleculas[molecula][z]
                 , cadeias[aa][x], cadeias[aa][y], cadeias[aa][z])
            if d <= limiar:
                """vai imprimir cada residuo(aa) cada atomo que interage com a molecula e que tem a distancia menor que 4."""
                #print(d, cadeias[aa][res_name], cadeias[aa][res_seq],moleculas[molecula][name])
                sitio.append(cadeias[aa][res_name]+ str(cadeias[aa][res_seq]))
    return sitio






# PROGRAMA PRINCIPAL
linhas = le_arquivo('5gwz.pdb')
# print(linhas)  # Imprime o arquivo como ele é, com quebra de linhas, etc.
# imprime_arquivo(linhas)
cadeias = obtem_cadeia(linhas, cadeia='A')
moleculas = obtem_molecula(linhas, 'PJE')
sitio_de_ligacao = set(obtem_sitio_ligacao(moleculas, cadeias, 4))
print(sitio_de_ligacao)
# sitio_de_ligacao_sem_rep = set(sitio_de_ligacao)
# print(sitio_de_ligacao_sem_rep)