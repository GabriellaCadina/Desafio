# criar funcao de saque, extrato e deposito
# criar funcao de cadastrar usuario e cadastrar conta bancaria

SAQUE_DIARIO = 3
numero_de_contas = 0

def cadastro_usuario():
# armazenar em lista/dictnome, cpf(somente numeros e n pode 2 cpfs iguais), data nascimento, endereco(rua, numero, bairro, cidade, sigla estado)
    lista_usuarios = []
    nome = input('Insira o seu nome completo: ')
    cpf = input('Insira o seu CPF: ').replace(".", "").replace("-","")
    data_nascimento = input('Insira sua data de nascimento: ')
    endereco = input('Insira seu endereço (nome da rua, número, bairro, cidade e sigla do estado): ')
    print('\nUsuário cadastrado com sucesso!\n')
    dicionario_usuario = {
        "nome" : nome ,
        "cpf" : cpf ,
        "data_de_nascimento" : data_nascimento,
        "endereco" : endereco
    }

    lista_usuarios.append(dicionario_usuario)
    print(lista_usuarios)


    return dicionario_usuario

def cadastro_conta(numero_da_conta):
    # vincular com o usuario
    # armazenar em lista, agencia(0001), numero da conta e user(pode ter mais de uma conta mas a conta pertence somente a um user)
    dicionario_conta = {
        "agencia" : "0001",
        "numero_conta" : numero_da_conta,
        "saldo" : 0,
        "limite_por_saque" : 500,
        "total_saques" : 0,
        "extrato" : "",
    }
    print('\nConta cadastrada com sucesso!\n')
    return dicionario_conta

def menu(conta_bancaria):
    while True:
        opcao_usuario = input('''
Seja Bem Vindo ao Gabi's Bank!\n
Selecione uma das opções abaixo para prosseguirmos com o seu atendimento:\n
1. Depósito
2. Saque
3. Extrato Bancário
4. Sair\n
''')
        if opcao_usuario == '1':
            deposito(conta_bancaria)
            
        elif opcao_usuario == '2':
            saque(conta_bancaria)
           
        elif opcao_usuario == '3':
            exibir_extrato(conta_bancaria)
        
        elif opcao_usuario == '4':
            break

        else:
            print('Opção inválida. Por gentileza, selecione a opção desejada.')
        
def deposito(conta_bancaria):
    valor_a_ser_depositado = float(input('Qual valor você deseja depositar?\n'))
    if valor_a_ser_depositado > 0:
        conta_bancaria["saldo"] += valor_a_ser_depositado
        conta_bancaria["extrato"] = conta_bancaria["extrato"] + f'Depósito: R$ {valor_a_ser_depositado:.2f}\n'
        print('Valor depositado com sucesso!')
    else:
        print('Valor inválido para depósito.')

def saque(conta_bancaria):
    valor_a_ser_sacado = float(input('Qual valor deseja sacar?\n'))
    if valor_a_ser_sacado > conta_bancaria["saldo"]:
        print('Valor para saque insuficiente.')
    elif valor_a_ser_sacado > conta_bancaria["limite_por_saque"]:
        print('O valor a ser sacado ultrapassou o limite diário.')
    elif conta_bancaria["total_saques"] >= SAQUE_DIARIO:
        print('Limite de saques diários atingido.')
    else:
        conta_bancaria["saldo"] -= valor_a_ser_sacado
        conta_bancaria["total_saques"] += 1
        conta_bancaria["extrato"] = conta_bancaria["extrato"] + f'Saque: R$ {valor_a_ser_sacado:.2f}\n'
        print('Valor sacado com sucesso!')

def exibir_extrato(conta_bancaria):
    print('################ EXTRATO ################')
    print("Não foram realizadas movimentações." if not conta_bancaria["extrato"] else conta_bancaria["extrato"])
    print(f"\nSaldo: R$ {conta_bancaria["saldo"]:.2f}")
    print('#########################################')


usuario = cadastro_usuario()
numero_de_contas += 1
conta = cadastro_conta(numero_de_contas)
menu(conta)

