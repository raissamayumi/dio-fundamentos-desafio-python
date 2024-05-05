menu1 = """

[1] Logar
[2] Criar Nova Usuario
[3] Criar Nova Conta
[0] Sair

=> """

menu2 = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """


def criar_usuario(usuarios):
    cpf =str(input("Informa o CPF "))

    usuario_existe = verificar_usuario(cpf, usuarios)
    if usuario_existe:
        print("Usuário já cadastrado")
        return 
    
    nome = input("Informa o nome completo ")
    usuarios.append({"cpf": cpf,"nome": nome})
    print("Usuário cadastrado com sucesso")
    return usuarios

def criar_conta_corrente(usuarios, contas, numero_conta):
    usuario_cpf = input("Informa o CPF ")

    usuario_existe = verificar_usuario(usuario_cpf, usuarios)
    if usuario_existe is None:
        print("Usuário não encontrado")
        return 

    contas.append({"numero_conta": numero_conta, "usuario_cpf": usuario_cpf})
    print(f"Conta de número: {numero_conta} cadastrada com sucesso")
    return contas


def verificar_se_conta_existe(numero_conta, contas):
    conta_filtrado = [conta for conta in contas if conta["numero_conta"] == numero_conta]
    return conta_filtrado[0] if conta_filtrado else None

def verificar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def depositar(saldo, valor, extrato):   
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Erro. O valor informado é inválido para depósito.")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Erro. Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Erro. O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Erro. Número limite de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Erro. O valor informado é inválido.")

    return saldo, extrato

def extrato(saldo,*,extrato):
    print("\n---EXTRATO---")
    print("Não foram registradas movimentações hoje." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("----------------")
    return None


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
numero_conta = 1
LIMITE_SAQUES = 3
while True:

    opcao1 = input(menu1)

    if opcao1 == "1":
        numero= input("Informe a conta: ")
        con = verificar_se_conta_existe(numero, contas)
        if con:
            opcao = input(menu2)

            if opcao == "1":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "2":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

            elif opcao == "3":
                extrato(saldo, extrato=extrato)

            elif opcao == "0":
                break

            else:
                print("Operação inválida.")
        else:
            print("Conta não encontrada.")

    if opcao1 == "2":
        usuarios = criar_usuario(usuarios)

    elif opcao1 == "3":
        contas = criar_conta_corrente(usuarios, contas, numero_conta)
        numero_conta = numero_conta +1

    elif opcao1 == "0":
     break

