"""
04252011000110 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
from functools import reduce


def so_num(msg):
    conv1 = msg.replace('.', '')
    conv2 = conv1.replace('/', '')
    conv3 = conv2.replace('-', '')
    return conv3


def digitos():
    for valor in cnpj_fracionado:
        lista3.append(int(valor))
    if len(lista3) == 12:
        lista4 = [(x * y) for x, y in zip(lista3, lista1)]
        soma = reduce(lambda ac, v: v + ac, lista4, 0)
    elif len(lista3) == 13:
        lista4 = [(x * y) for x, y in zip(lista3, lista2)]
        soma = reduce(lambda ac, v: v + ac, lista4, 0)
    else:
        return
    digito = str(11 - (soma % 11))
    if int(digito) > 9:
        digito = '0'
    lista3.clear()
    return digito


cnpj = input('Digite o CNPJ para a validação: ').strip()
cnpj_preliminar = so_num(cnpj)
cnpj_fracionado = cnpj_preliminar[0:-2]

lista1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista3 = []

cnpj_fracionado = cnpj_fracionado + digitos()
cnpj_fracionado = cnpj_fracionado + digitos()

if cnpj_fracionado == cnpj_preliminar:
    print('O CNPJ é válido')
else:
    print('O CNPJ é inválido')
