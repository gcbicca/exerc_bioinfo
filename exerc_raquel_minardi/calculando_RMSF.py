"""É O DESVIO QUADRÁTICO MÉDIO ENTRE AS COORDENADAS ATOMICAS TRIDIMENSIONAIS DE UMA
ESTRUTURA EM DIVERSOS MOMENTOS DO TEMPO t. É COMPUTADA PARA CADA ATOMO.
É USADA PARA ANALISAR O QUANTO CADA ATOMO FLUTUA AO LONGO DE UMA SIMULAÇÃO DE DINAMICA MOLECULAR."""
from math import sqrt
import matplotlib.pyplot as plt


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
            atoms[serial] = (x, y, z)
    return atoms


def rmsf(modelo_referencia, num_modelos, linhas):  #modelos_referencia vai receber a posicao de escolha do modelo de referencia dentro da lista modelos.
    modelos = []
    modelos.append(None)  # Deixa a posicao 0 vazia.
    # Obtem todos os num_modelos de linhas e armazena na lista.
    for i in range(1, num_modelos + 1):
        modelos.append(obtem_modelo(i, linhas))
    # temos que ter a soma para acada atomo, as flutuacoes de cada um
    soma = []
    for i in range(0, len(modelos[modelo_referencia])+1):  # Percorre todos os atomos do modelo, sendo os modelos de == tamanho.
        soma.append(0)  # Cria uma lista zerada com o tamnho do n de atomos.
    x = 0
    y = 1
    z = 2
    for i in range(1, num_modelos + 1):  # Para cada modelo
        for atom in range(1, len(modelos[modelo_referencia])+1):  # Para cada atomo for atom in range(1, len(modelos[modelo_referencia]) + 1):  # Para cada atomo
            if i != modelo_referencia:  # Modelos diferentes do modelo_referencia
                soma[atom] += (modelos[i][atom][x] - modelos[modelo_referencia][atom][x])**2 + (modelos[i][atom][y] - modelos[modelo_referencia][atom][y])**2 + (modelos[i][atom][z] - modelos[modelo_referencia][atom][z])**2  #soma[1] += modelos[1][1][0]
    for atom in range(1, len(modelos[modelo_referencia])+1):  # Para cada atomo
        soma[atom] = sqrt(soma[atom]/num_modelos)  # t é o num_modelos, figindo que os 10 modelos sao um intervalo de tempo
    soma.remove(0)
    return soma


def plota_rmsf(rmsf):
    y_axis = rmsf
    x_axis = []
    for i in range(1, len(y_axis)+1):
        x_axis.append(i)
    plt.plot(x_axis, y_axis)
    plt.title('ROOT MEAN SQUARE FLUCTUATION (RMSF)')
    plt.xlabel('ATOM')
    plt.ylabel('RMSF (ANSGTROMS)')
    plt.show()


# PROGRAMA PRINCIPAL
linhas = le_arquivo('2m6q.pdb')
# imprime_arquivo(linhas)
mod = obtem_modelo(1, linhas)
print(mod)
rmsf = rmsf(1, 10, linhas)
plota_rmsf(rmsf)