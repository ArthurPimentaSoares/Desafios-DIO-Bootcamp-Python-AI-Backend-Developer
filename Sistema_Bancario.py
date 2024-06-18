saldo = 0
extrato = ""
limite = 500
numeros_saques = 0
LIMITE_SAQUES = 3

while True :
    menu = int(input("""

[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair
"""))
    if (menu == 1):
        valor = float(input("Digite a quantia do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += (f"Deposito: R$ {valor:.2f}\n")
            print("\nDeposito completo!!!")
        else:
            print("O valor digitado é invalido!")
        
    elif (menu == 2):
        valor = float(input("informe o valor do saque: "))
        saldo_exedido = valor > saldo
        limite_exedido = valor > limite
        max_saques = numeros_saques >= LIMITE_SAQUES

        if saldo_exedido:
            print('Saldo insuficiente!')
        elif limite_exedido:
            print("O valor do saque exedeu o limite!")
        elif max_saques:
            print("Números maxímo de saques exedido!")
        elif (valor > 0) :
            saldo -= valor 
            extrato += (f"Saque: R$ {valor:.2f}\n")
            numeros_saques += 1
            print("\nSaque completo!!!")
        else:
            print("O valor informado é invalido.")

    elif (menu == 3):
        print("--------------EXTRATO--------------")
        print("Não foram realizados movimentações."if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("-------------------------------------")
    elif (menu == 0):
        break
    else:
        print("Opção invalida! Escolha outra opção.")
