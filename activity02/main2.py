frutas = set()


frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

pesquisa = input("digite o nome da fruta:")
if pesquisa:
    print(f"fruta encontrada: {pesquisa}")
else:
    print(f"não encontrado: {pesquisa}")