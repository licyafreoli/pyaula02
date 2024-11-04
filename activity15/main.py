def uniao_conjuntos(*conjuntos):
    return set().union(*conjuntos)

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto3 = {5, 6, 7}
print(uniao_conjuntos(conjunto1, conjunto2, conjunto3))
