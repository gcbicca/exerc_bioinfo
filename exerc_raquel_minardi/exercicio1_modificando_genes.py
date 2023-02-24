import sys
import re

"""Vamos inserir as mutações no gene correspondente"""


# # ABRIR O ARQUIVO
# with open("sequence.txt", 'r') as f:
#     f = f.read()


# ABRIR ARQUIVO COMO FUNCAO
def abrir_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as f:
        linha = f.read()
        linha = list(linha.rstrip())   # Transformo o arquivo lido em uma lista e removo a quebra no final se houver.
        linha.insert(0, '-')
        return linha


def ler_arquivo_mutacoes(nome_arquivo):
    with open(nome_arquivo) as f:
        linha = f.read()
        linha = linha.rstrip()
        mutacoes = linha.split(', ')   # Removo os caracteres ,espaço, e guardo na variavel mutacoes
        return mutacoes


def substituicao(lista, aa1, aa2, pos):
# Testando se na posicao da lista tem o aa indicado
    if (lista[pos]) != aa1:
        print(f'ERRO: {aa1} nao esta na posicao {pos}')
        exit()
    else:
        lista[pos] = aa2


def inserindo_mutacoes(lista, mutacoes):
    for mutacao in mutacoes:
        if mutacao[0:3] != "del" and mutacao[0:3] != 'ins':
            aa1 = mutacao[0]
            aa2 = mutacao[-1]
            pos = int(mutacao[1:-1])
# PODERIA SE UTILIZAR AGR APENAS O CODIGO PARA SUBSTITUIR, MAS VAMOS ENCAPSULAR O CODIGO MELHOR E FAZER TESTES
            #lista[pos] = aa2
# UTILIZAREMOS UMA FUNCAO
            substituicao(lista, aa1, aa2, pos)


def deleta(lista, pos):
    lista[pos] = '-'


def faz_delecoes(lista, mutacoes):
    """nao iremos deletar as mutacoes da lista mas inseriri um gap"""
    for mutacao in mutacoes:
        if mutacao[0:3] == 'del':
            mutacao = mutacao.lstrip('del')  # del69-70 -> 69-70
            tmp = mutacao.split('-')  #69-70 -> [69, 70]
            pos1 = int(tmp[0])
            if len(tmp) > 1:
                pos2 = int(tmp[1])  # pode ser vazio
            for posicao in range(pos1, pos2+1):
                deleta(lista, posicao)


"""Faremos as inserções do ultimo ao primeiro, para nao alterar o indice da sequencia"""
def insere(lista,pos,aa):
    lista.insert(pos, aa)


def faz_insercoes(lista,mutacoes):
    for mutacao in range(len(mutacoes)-1, -1, -1):
        if mutacoes[mutacao][0:3] == 'ins':  #ins214EPE
            mutacao = mutacoes[mutacao].lstrip('ins')  # ins214EPE -> 214EPE
            pos = re.sub(r'\D', '', mutacao)
            #pos = re.search('[\d]+', mutacao)  #\d= bucando digitos, "+" buscando mais de um digitos numericos
            #pos=int(pos.group())
            pos = int(pos)
            #seq = re.search('[A-Z]+', mutacao)
            seq = re.sub('[^a-zA-Z]+', '', mutacao)
            seq = list(seq)
            """Se eu inserir os aa na sequencia, ele irao ao estar na posicao invertida"""
            seq.reverse()
            for aa in seq:
                insere(lista, pos, aa)


def gera_sequencia_final(lista):
    seq = ''
    for i in lista:
        if i != '-':
            seq += i
    return seq


def imprime_comparativo(seq1, seq2):
    tam = min(len(seq1), len(seq2))
    for i in range(0,tam):
        print(i+1, seq1[1:-1][i], seq2[i])

# PROGRAMA PRINCIPAL

# if len(sys.argv) != 3:
#     print('USAGE: python3 <sequencias><mutacoes>')
#     exit()

#MODO SEM A UTILIZACAO DE SYS
lista_original = abrir_arquivo('sequence.txt')
mutacoes = ler_arquivo_mutacoes('mutations.txt')
lista_mut = lista_original.copy()   # Copia da lista original
inserindo_mutacoes(lista_mut, mutacoes)
faz_delecoes(lista_mut, mutacoes)
faz_insercoes(lista_mut, mutacoes)
lista_final = gera_sequencia_final(lista_mut)
imprime_comparativo(lista_original, lista_final)

# for i in range(0, len(lista_original)):  #lista original sempre vai ser maior, mas teremos o - na mutada
#     #if i == [100]:
#         print(i, lista_original[i], lista_mut[i])

# # MODO UTILIZANDO O SYS
# lista_original = abrir_arquivo(sys.argv[1])
# mutacoes = ler_arquivo_mutacoes(sys.argv[2])
# lista_mut = lista_original.copy()
# inserindo_mutacoes(lista_mut,mutacoes)
