convidados = [
    "Carlos", "Ana", "João", "Mariana", "Pedro", "Laura", "Lucas", "Fernanda", "Roberto", "Camila"
]

convites = (
    "A34B89", "C57Z31", "D92X74", "E81Y65", "F03V28", "G56W49", "H77T12", "J88Q34", "K19L53", "L20M67"
)
while True: 
    print("Lista de Convidados: ")
    for i, convidado in enumerate(convidados):
        print(f"{i + 1}. {convidado}")

    posicao_convidado = float(int(input("\nDigite o número respectivo do convidado (1 - 10): ")))

    if posicao_convidado >= 1 and posicao_convidado <=10:
        numero_convite = convites[posicao_convidado - 1]
        print(f"O convite do convidado {convidados[posicao_convidado - 1]} é: {numero_convite}")
    else:
        print("Número digitado invalido. Por favor, tente novamente.")    
     except ValueError:
         print("Por favor, digite um número válido ou 'sair' para encerrar.")
    