registros_humor = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar humor")
    print("2. Meus registros de humor")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        data = input("Digite a data do registro: ")
        hora = input("Digite a hora do registro: ")
        humor = input("Em uma escala de 1 a 10, como está seu humor agora? ")
        emocao = input("Quais emoções você está sentindo? (ex: alegria, ansiedade, raiva...) ")
        observacao = input("Quer deixar alguma observação? ")

        registro = {
            'data': data,
            'hora': hora,
            'humor': humor,
            'emocao': emocao,
            'observacao': observacao
        }

        registros_humor.append(registro)
        print("Humor registrado com sucesso!")

    elif escolha == '2':
        if registros_humor:
            print("\nSeus registros de humor:")
            for i, registro in enumerate(registros_humor, 1):
                print(f"\nRegistro {i}:")
                print(f" Data: {registro['data']}")
                print(f" Hora: {registro['hora']}")
                print(f" Nível de humor: {registro['humor']}")
                print(f" Emoções: {registro['emocao']}")
                print(f" Observações: {registro['observacao']}")
        else:
            print("\nVocê ainda não registrou seu humor.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de humor encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
