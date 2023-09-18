import os

contas = [0]
LIMITE_SAQUE = 3
VALOR_MAXIMO_SAQUE = 500

def main():
    cadastro = {}
    escolha = 0

    while escolha != 7:
        os.system("clear")
        escolha = int(input('''====================== MENU =======================
 1. Fazer cadastro
 2. Criar Conta
 3. Depósito
 4. Saque
 5. Extrato
 6. Listar contas
 7. Sair 
=> '''))
          
        if escolha == 3:
            deposito(cadastro)
        elif escolha == 4:
            saque(cadastro)
        elif escolha == 5:
            extrato(cadastro)
        elif escolha == 6:
            listar_contas(cadastro)
            
        elif escolha == 1:
            novo_cadastro(cadastro)
        elif escolha == 2:
                criar_conta(cadastro)
        elif escolha == 7: print("Saindo...")

def novo_cadastro(cadastro):
    os.system("clear")
    cpf_digitado, busca = pesquisar_cpf(cadastro)
    if busca:
        print("CPF existente")
    else:
        nome_digitado = input("Digite seu nome e sobrenome: ")
        data_digitado = input("Digite a data de nascimento (dd/MM/yyyy): ")
        salario_digitado = float(input("Digite a sua renda mensal: "))
        cadastro[cpf_digitado] = {
            "nome": nome_digitado,
            "data_nascimento": data_digitado,
            "salario": salario_digitado,
            "contas": []  # Lista para armazenar as contas associadas ao CPF
        }
        input("CPF cadastrado com sucesso, pressione enter para continuar_")

def pesquisar_cpf(cadastro):
    cpf_digitado = input("Digite o seu CPF (somente números): ")
    busca = cadastro.get(cpf_digitado)
    return cpf_digitado, busca

def criar_conta(cadastro):
    os.system("clear")
    cpf_digitado, busca = pesquisar_cpf(cadastro)
    if not busca:
        print("CPF não possui cadastro. Cadastre-se primeiro.")
    else:
        agencia = input('''Escolha uma Agência
1. 01
2. 02
3. 03
=> ''').zfill(2)

        salario_SN = int(input('''Gostaria de trazer seu sálario para agência? 
1. Sim
2. Não
=> '''))
        saldo = busca["salario"] if salario_SN == 1 else 0
        ultima_conta = max(contas) + 1
        contas.append(ultima_conta)
        conta = str(ultima_conta).zfill(4)
        conta = conta[:3] + '-' + conta[3:]
        nova_conta = {
            "agencia": agencia,
            "conta": conta,
            "saldo": saldo,
            "extrato": []
        }
        busca["contas"].append(nova_conta)
        input(f"Conta: {conta} cadastrada com sucesso.\nPressione enter para continuar_")
        return nova_conta

def listar_contas(cadastro):
    os.system("clear")
    print("Lista de todas as contas cadastradas:")
    for cpf, info in cadastro.items():
        print(f"CPF: {cpf}")
        for conta in info["contas"]:
            print(f"Agência: {conta['agencia']}, Conta: {conta['conta']}, Saldo: R$ {conta['saldo']:.2f}")
    input("Pressione enter para continuar_")

def deposito(cadastro):
    os.system("clear")
    cpf_digitado, busca = pesquisar_cpf(cadastro)
    if not busca:
        print("CPF não possui cadastro")
        input("Pressione enter para continuar_")
    else:
        conta_digitada = input("Digite o número da conta: ")
        conta = encontrar_conta(busca["contas"], conta_digitada)
        if not conta:
            print("Conta não encontrada")
            input("Pressione enter para continuar_")
 
        else:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                conta["saldo"] += valor
                conta["extrato"].append(f"Depósito de {valor}")
                print("Valor depositado realizado com sucesso.")
                input("Pressione enter para continuar_")
            else:
                print("Valor do depósito é inválido.")
                input("Pressione enter para continuar_")

def saque(cadastro):
    os.system("clear")
    cpf_digitado, busca = pesquisar_cpf(cadastro)
    if not busca:
        print("CPF não possui cadastro")
        input("Pressione enter para continuar_")
    else:
        conta_digitada = input("Digite o número da conta: ")
        conta = encontrar_conta(busca["contas"], conta_digitada)
        
        if conta is None:
            print("Conta não encontrada")
            input("Pressione enter para continuar_")
        else:
            saques_realizados = sum(1 for transacao in conta.get("extrato", []) if "Saque" in transacao)
            if saques_realizados >= LIMITE_SAQUE:
                print("Você atingiu o limite de saque.")
            elif conta["saldo"] <= 0:
                print("Sem saldo na conta")
                input("Pressione enter para continuar_")
            else:
                valor = float(input("Digite o valor do saque: "))
                if valor > 0 and valor <= conta["saldo"] and valor <= VALOR_MAXIMO_SAQUE:
                    conta["saldo"] -= valor
                    conta["extrato"].append(f"Saque de {valor}")
                    print(f"Saque de {valor} realizado com sucesso.")
                    input("Pressione enter para continuar_")
                else:
                    print("Valor do saque é inválido ou superior ao saldo disponível.")
                    input("Pressione enter para continuar_")
def extrato(cadastro):
    os.system("clear")
    cpf_digitado, busca = pesquisar_cpf(cadastro)
    if not busca:
        print("CPF não possui cadastro")
    else:
        conta_digitada = input("Digite o número da conta: ")
        conta = encontrar_conta(busca["contas"], conta_digitada)
        if not conta:
            print("Conta não encontrada")
        else:
            os.system("clear")
            print("====================== Extrato =======================")
            print(f"Extrato da conta {conta['conta']} - Saldo: R$ {conta['saldo']:.2f}")
            print("Histórico de transações:")
            for transacao in conta["extrato"]:
                print(transacao)
            print("======================================================")
            input("Pressione enter para continuar_")

def encontrar_conta(contas, numero_conta):
    for conta in contas:
        if conta["conta"] == numero_conta:
            return conta
    return None

main()
