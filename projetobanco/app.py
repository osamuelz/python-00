from limpar import limpar_tela, validar_cpf, validar_data, verificar_maioridade

usuarios_banco = {}

def criar_conta():
    limpar_tela()
    print("--- CADASTRO DE NOVA CONTA ---")
    
    cpf = input("Digite o CPF (apenas números): ").strip()
    if not validar_cpf(cpf):
        print("❌ CPF inválido!"); input("\n[Pressione Enter]"); return
    
    if cpf in usuarios_banco:
        print("❌ Este CPF já possui uma conta."); input("\n[Pressione Enter]"); return

    data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
    if not validar_data(data_nasc) or not verificar_maioridade(data_nasc):
        print("❌ Data inválida ou você é menor de 18 anos."); input("\n[Pressione Enter]"); return

    senha = input("Crie sua senha: ").strip()
    
    usuarios_banco[cpf] = {
        "senha": senha,
        "nascimento": data_nasc,
        "saldo": 100.0
    }
    
    print("\n✅ Conta criada com sucesso! Você recebeu um bônus de R$ 100,00.")
    input("\n[Pressione Enter para voltar ao menu]")

def menu_operacoes(cpf_logado):
    """Este menu tem seu próprio loop 'while' para não deixar o usuário sair"""
    while True:
        limpar_tela()
        conta = usuarios_banco[cpf_logado]
        print(f"--- ÁREA LOGADA | CPF: {cpf_logado} ---")
        print(f"SALDO: R$ {conta['saldo']:.2f}")
        print("1. Depósito")
        print("2. Saque")
        print("3. Sair da conta (Logout)")
        
        op = input("\nEscolha: ")
        
        if op == "1":
            valor = float(input("Quanto depositar? "))
            conta['saldo'] += valor
            input("✅ Sucesso! [Enter]")
        elif op == "2":
            valor = float(input("Quanto sacar? "))
            if valor <= conta['saldo']:
                conta['saldo'] -= valor
                input("✅ Sucesso! [Enter]")
            else:
                input("❌ Saldo insuficiente! [Enter]")
        elif op == "3":
            print("Efetuando logout...")
            break

def login():
    limpar_tela()
    print("--- LOGIN ---")
    cpf_digitado = input("CPF: ").strip().replace(".", "").replace("-", "")
    senha_digitada = input("Senha: ").strip()

    if cpf_digitado in usuarios_banco:
        if usuarios_banco[cpf_digitado]["senha"] == senha_digitada:
            print("\n✅ Acesso concedido!")
            menu_operacoes(cpf_digitado) 
        else:
            print("\n❌ Senha incorreta.")
            input("\nPressione Enter para voltar...")
    else:
        print("\n❌ CPF não encontrado.")
        input("\nPressione Enter para voltar...")
        print("\n❌ Este CPF não está cadastrado ou formato inválido.")
        input("[Enter para voltar]")

def menu_principal():
    while True:
        limpar_tela()
        print(" ---CAIXA ELETRÔNICO--- ")
        print("1. Criar Conta (R$ 100 de bônus)")
        print("2. Entrar na Conta")
        print("3. Encerrar")
        
        escolha = input("\nSelecione: ")

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            login()
        elif escolha == "3":
            break

if __name__ == "__main__":
    menu_principal()