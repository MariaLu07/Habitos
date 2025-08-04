meus_medicamentos = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar medicamento")
    print("2. Meus medicamentos")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        medicamento = input("Digite o nome de seu novo medicamento: ")
        dosagem_input = input("Digite a dosagem (em ml ou mg): ")

        try:
            dosagem = float(dosagem_input)
            data_inicio = input("Digite a data de início do tratamento: ")
            data_fim = input("Digite a data de término do tratamento: ")
            orientacoes = input("Quais as orientações desse remédio? ")

            registro = {
                "medicamento": medicamento,
                "dosagem": dosagem,
                "data_inicio": data_inicio,
                "data_fim": data_fim,
                "orientacoes": orientacoes
            }

            meus_medicamentos.append(registro)
            print("\nMedicamento registrado com sucesso!")

        except ValueError:
            print("Valor inválido para dosagem! Digite um número (ex: 5 ou 7.5).")

    elif escolha == '2':
        if meus_medicamentos:
            print("\nSeus medicamentos registrados:")
            for i, med in enumerate(meus_medicamentos, 1):
                print(f"\nMedicamento {i}:")
                print(f" Nome: {med['medicamento']}")
                print(f" Dosagem: {med['dosagem']}")
                print(f" Início: {med['data_inicio']}")
                print(f" Término: {med['data_fim']}")
                print(f" Orientações: {med['orientacoes']}")

        else:
            print("\nVocê ainda não registrou nenhum medicamento.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de medicamentos encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
