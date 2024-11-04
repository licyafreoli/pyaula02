def verificar_chaves(dicionario, lista_chaves):
    return all(chave in dicionario for chave in lista_chaves)

dicionario = {"a": 1, "b": 2, "c": 3}
lista_chaves = ["a", "b"]
print(verificar_chaves(dicionario, lista_chaves))
