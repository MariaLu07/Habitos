atividades_fisicas = []

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Registrar atividade física")
    print("2. Minhas atividades")
    print("3. Sair")

    escolha = input("\nDigite 1, 2 ou 3: ")

    if escolha == '1':
        data_hora = input("Digite a data e hora do início da atividade: ")
        duracao = input("Qual foi a duração da atividade?: ")
        distancia = input("Qual foi a distância percorrida? (em Km): ")
        calorias = input("Quantas calorias foram queimadas? ")

        registro = {
            'data_hora': data_hora,
            'duracao': duracao,
            'distancia': distancia,
            'calorias': calorias
        }

        atividades_fisicas.append(registro)
        print("Atividade registrada com sucesso!")

    elif escolha == '2':
        if atividades_fisicas:
            print("\nSuas atividades registradas:")
            for i, atividade in enumerate(atividades_fisicas, 1):
                print(f"\nAtividade {i}:")
                print(f" Data e Hora: {atividade['data_hora']}")
                print(f" Duração: {atividade['duracao']}")
                print(f" Distância: {atividade['distancia']}")
                print(f" Calorias queimadas: {atividade['calorias']}")
        else:
            print("\nVocê ainda não registrou nenhuma atividade.")

    elif escolha == '3':
        print("\nSaindo do programa. Registro de atividades encerrado!")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
