def adicionar_ao_dicionario(dicionario, chave, valor):
    dicionario[chave] = valor
    return dicionario

dicionario = {"a": 1, "b": 2}
chave = "c"
valor = 3
dicionario_atualizado = adicionar_ao_dicionario(dicionario, chave, valor)
print(dicionario_atualizado)
