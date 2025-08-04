configuracoes = {}

print("Bem-vindo ao seu app de bem-estar!")
print("Antes de começarmos, vamos configurar suas preferências:")

print("\nEscolha a unidade de peso:")
print("1. kg")
print("2. lbs")
while True:
    escolha_peso = input("Digite 1 ou 2: ")
    if escolha_peso == '1':
        configuracoes['peso_unidade'] = 'kg'
        break
    elif escolha_peso == '2':
        configuracoes['peso_unidade'] = 'lbs'
        break
    else:
        print("Opção inválida.")

print("\nEscolha a unidade de altura:")
print("1. cm")
print("2. m")
print("3. in")
while True:
    escolha_altura = input("Digite 1, 2 ou 3: ")
    if escolha_altura == '1':
        configuracoes['altura_unidade'] = 'cm'
        break
    elif escolha_altura == '2':
        configuracoes['altura_unidade'] = 'm'
        break
    elif escolha_altura == '3':
        configuracoes['altura_unidade'] = 'in'
        break
    else:
        print("Opção inválida.")

print("\nEscolha o tema do app:")
print("1. Claro")
print("2. Escuro")
while True:
    escolha_tema = input("Digite 1 ou 2: ")
    if escolha_tema == '1':
        configuracoes['tema'] = 'claro'
        break
    elif escolha_tema == '2':
        configuracoes['tema'] = 'escuro'
        break
    else:
        print("Opção inválida.")

print("\nConfigurações salvas com sucesso!")
print("Resumo das suas preferências:")
print(f" - Unidade de peso: {configuracoes['peso_unidade']}")
print(f" - Unidade de altura: {configuracoes['altura_unidade']}")
print(f" - Tema do app: {configuracoes['tema']}")
