menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Valor inválido! Por favor insira um valor válido.")
        except ValueError:
            print("Valor inválido! Por favor insira um valor numérico válido")
            
    elif opcao == "2":
        try:
            valor = float(input("Digite o valor que deseja sacar: "))            

            if valor > saldo:
                print("Operação não realizada! Você não possui saldo suficiente.")

            elif valor > limite:
                print("Valor de saque excedido! insira um valor permitido.")

            elif numero_saques >= LIMITE_DE_SAQUE:
                print("Operação não realizada! Limite de saque excedido")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
        except ValueError:
            print("Valor inválido! Por favor insira um valor numérico válido")      

    elif opcao == "3":
        print("\n***EXTRATO***")
        
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print("***SALDO***")
            print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione a opção desejada.")
