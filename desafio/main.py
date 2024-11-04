def cadastrar_aluno(alunos, nome, idade, notas):
    alunos[nome] = {"idade": idade, "notas": notas}
    return alunos

alunos = {}
cadastrar_aluno(alunos, "João", 16, [8, 9, 7])
cadastrar_aluno(alunos, "Maria", 17, [10, 8, 9])
print(alunos)
def calcular_media(notas):
    return sum(notas) / len(notas)

def exibir_alunos(alunos):
    for nome, dados in alunos.items():
        media = calcular_media(dados["notas"])
        print(f"Aluno: {nome}, Idade: {dados['idade']}, Média: {media}")

def melhor_aluno(alunos):
    return max(alunos.items(), key=lambda x: calcular_media(x[1]["notas"]))

alunos = {
    "João": {"idade": 16, "notas": [8, 9, 7]},
    "Maria": {"idade": 17, "notas": [10, 8, 9]},
    "Carlos": {"idade": 16, "notas": [6, 7, 8]}
}
exibir_alunos(alunos)
print("Melhor aluno:", melhor_aluno(alunos)[0])
