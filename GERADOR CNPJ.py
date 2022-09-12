from random import randint
from functools import reduce


def gera():
    string = ''
    for c in range(0, 12):
        digito = randint(0, 9)
        string += str(digito)
    return string


def digitos():
    for valor in cnpj:
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


lista1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
lista3 = []

iniciar = input('Digite "G" para gerar um CNPJ: ').strip().upper()
if iniciar != "G":
    print('Volte Sempre')
else:
    cnpj = gera()
    cnpj = cnpj + digitos()
    cnpj = cnpj + digitos()

print(cnpj)
