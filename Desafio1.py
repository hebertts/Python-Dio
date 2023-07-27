import os
barra = "="
MENU = """[d] - Depositar    ->
[s] - Sacar        ->
[e] - Extrato      ->
[q] - Sair         ->
"""+ barra.center(40,barra) +"\n=> "
title = " Sistema Bancário "
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    os.system('clear')
    print(title.center(40,barra))
    opcao = input(MENU)

    if opcao == "d":
        
        os.system('clear')
        print(title.center(40,barra))
        print("- Caixa > Deposito\n")
        print(f"\nSaldo da Conta: R$ {saldo:.2f}")
        print(barra.center(40,barra))
        valor = float(input("\nInforme o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("\nValor informado é inválido")
            input("\nPressione enter para continuar_")
            os.system('clear')
    
    elif opcao == "s":
        if saldo > 0:
            
            os.system('clear')
            print(title.center(40,barra))
            print("- Caixa > Sacar\n")
            print(f"\nSaldo na conta: R$ {saldo:.2f}")
            print(barra.center(40,barra))
            saque = float(input("Digite o valor de saque: "))
             
            excedeu_limite = saque > limite

            excedeu_saque = numero_saques >= LIMITE_SAQUES
        
            excedeu_saldo = saque > saldo

            if excedeu_limite:
                
                print("\nValor informado é maior que o limite de R$500,00")
                input("\nPressione enter para continuar_")
                os.system('clear')
                
            elif excedeu_saldo:
                
                print("\nValor informado maior que o saldo disponível")
                input("\nPressione enter para continuar_")
                os.system('clear')
                
               
            elif excedeu_saque:
                
                print("\nLimite de saque diário atingido")
                input("\nPressione enter para continuar_")
                os.system('clear')
                
            
            elif saque > 0:
                saldo -= saque
                numero_saques = numero_saques + 1
                extrato += f"Extrato: R$ {saque:.2f}\n"
            
            elif saque < 0:
                print("\nValor informado inválido")
                input("\nPressione enter para continuar_")
                os.system('clear')                
                
        else:
            os.system('clear')
            print(title.center(40,barra))
            print("- Caixa > Sacar\n")
            print("\nSem saldo na conta")
            print(barra.center(40,barra))
            
            input("\nPressione enter para continuar_")
            os.system('clear')

    elif opcao == "e":
        if extrato == "":
            
            os.system('clear')
            print(title.center(40,barra))
            print("- Extrato\n")
            print(" Sem movimentação na conta")
            print(barra.center(40,barra))
            input("\nPressione enter para continuar_")
            os.system('clear')
           
        else:      
            os.system('clear')
            print(title.center(40,barra))
            print(f'''- Extrato               Saldo: R$ {saldo:.2f}\n''')
            print(extrato)
            print(barra.center(40,barra))
            input("\nPressione enter para continuar_")
            os.system('clear')
            

    elif opcao == "q":
        break
