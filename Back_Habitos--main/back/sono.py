registro_sono = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar sono")
    print("2. Meus registros de sono")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        data = input("Digite a data do registro: ")
        hora_inicio = input("Digite a hora inicial do sono: ")
        hora_final = input("Digite a hora final do sono: ")
        qualidade = input("Digite a qualidade do seu sono (de 1 a 10): ")
        observacoes = input("Digite alguma observação do seu sono: ")

        registro = {
            'data': data,
            'hora_inicio': hora_inicio,
            'hora_final': hora_final,
            'qualidade': qualidade,
            'observacoes': observacoes
        }

        registro_sono.append(registro)
        print("Sono registrado com sucesso!")

    elif escolha == '2':
        if registro_sono:
            print("\nSeus registros de sono:")
            for i, registro in enumerate(registro_sono, 1):
                print(f"\nRegistro {i}:")
                print(f" Data: {registro['data']}")
                print(f" Hora inicial: {registro['hora']}")
                print(f" Hora final: {registro['quantidade']}")
                print(f" Qualidade: {registro['quantidade']}")
                print(f" Hora final: {registro['quantidade']}")
        else:
            print("\nVocê ainda não registrou nenhum sono.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de sono encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
