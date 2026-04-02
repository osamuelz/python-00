import os

def limpar():
    os.system("cls")

saldo = 100.0 

def deposito():
    global saldo
    try:
        valor = float(input("digite quanto você quer depositar: "))
        if valor <= 0:
            print("o valor deve ser maior que zero")
        else:
            saldo += valor
            print(f"deposito de R$ {valor} realizado.")
    except ValueError:
        print("digite os numeros corretamente")

def sacar():
    global saldo
    try:
        valor_saque = float(input("digite quanto você quer sacar: "))
        if valor_saque <= 0:
            print("valor invalido")
        elif valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque} realizado com sucesso!")
        else:
            print("Saldo insuficiente")
    except ValueError:
        print("Digite os numeors corretamente")

def consulta():
    print(f"\n - Extrato -")
    print(f"Saldo atual: R$ {saldo}")

cadastro_user = "caio"
cadastro_senha = "1234"
logado = False

while not logado:
    usuario = input("Digite o nome da conta: ")
    senha = input("Digite sua senha: ")

    if usuario == cadastro_user and senha == cadastro_senha:
        print("\nLogin realizado com sucesso")
        logado = True
    else:
        print("Dados incorretos")
        limpar() 

while logado:
    print("\n1 - Depósito | 2 - Saque | 3 - Consulta | 4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        deposito()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        consulta()
    elif opcao == '4':
        print("Encerrando...")
        break
    else:
        print("Opção inválida")