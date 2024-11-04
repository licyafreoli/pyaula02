alunos_notas = {"João": [8, 9, 7], "Maria": [10, 8, 9], "Carlos": [6, 7, 8]}
medias = {aluno: sum(notas) / len(notas) for aluno, notas in alunos_notas.items()}
print(medias)
