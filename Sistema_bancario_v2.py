saldo = 0.0
extrato = ""
limite = 500
numeros_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []
def deposito(saldo,valor,extrato,/):
    if valor > 0:
        saldo+=valor
        extrato += (f"Deposito: R$ {valor:.2f}")
        print("\nDeposito completo!!!")
    else:
        print("O valor digitado é invalido!")
    return(saldo, extrato)

def saque(*,saldo,valor,extrato,limite,numeros_saques,LIMITE_SAQUES):
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
    return(saldo,extrato)

def criar_usuario(usuarios):
    cpf = input("Digite seu CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com este CPF!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("informe sua data de nascimento (DD-MM-AAAA): ")
    endereco = input("Informe seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(AGENCIA,numero_conta,usuarios):
    cpf = input("informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia":AGENCIA,"numero_conta":numero_conta,"usuario":usuario}
    print("Usuario não encontrado, criação de conta encerrada!")

while True :
    menu = int(input("""
[1]Depositar
[2]Sacar
[3]Extrato
[4]Novo usuario
[5]Nova conta
[0]Sair
"""))
    if (menu == 1):
        valor = float(input("Digite a quantia do deposito: "))
        saldo,extrato = deposito(saldo,valor,extrato)
    elif (menu == 2):
        valor = float(input("informe o valor do saque: "))
        saldo, extrato = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numeros_saques=numeros_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )
    elif (menu == 3):
        print("--------------EXTRATO--------------")
        print("Não foram realizados movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------------")
    elif (menu == 4):
        criar_usuario(usuarios)
    elif (menu == 5):
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA,numero_conta,usuarios)
        if conta:
            contas.append(conta)
    elif (menu == 0):
        break
    else:
        print("Opção invalida! Escolha outra opção.")
    
