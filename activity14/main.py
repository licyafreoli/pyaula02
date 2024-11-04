def remover_duplicatas(lista):
    return list(set(lista))

lista_numeros = [1, 2, 2, 3, 4, 4, 5]
print(remover_duplicatas(lista_numeros))
