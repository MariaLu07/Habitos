minhas_refeicoes = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar refeição")
    print("2. Minhas refeições")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        alimento = input("Digite os alimentos do seu prato: ")
        carboidrato = input("Quantas gramas de carboidrato tem no seu prato? ")
        proteina = input("Quantas gramas de proteína tem no seu prato? ")
        gordura = input("Quantas gramas de gordura tem no seu prato? ")
        observacao = input("Você tem alguma observação a respeito da sua refeição? ")

        registro = {
            'alimento': alimento,
            'carboidrato': carboidrato,
            'proteina': proteina,
            'gordura': gordura,
            'observacao': observacao
        }

        minhas_refeicoes.append(registro)
        print("Refeição registrada com sucesso!")

    elif escolha == '2':
        if minhas_refeicoes:
            print("\nSuas refeições registradas:")
            for i, ref in enumerate(minhas_refeicoes, 1):
                print(f"\nRefeição {i}:")
                print(f" Alimentos do prato: {ref['alimento']}")
                print(f" Carboidrato: {ref['carboidrato']}")
                print(f" Proteína: {ref['proteina']}")
                print(f" Gordura: {ref['gordura']}")
                print(f" Observações: {ref['observacao']}")
        else:
            print("\nVocê ainda não registrou nenhuma refeição.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de refeições encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
