# Deposito- Deve ser possível depositar valores positivos para a minha conta bancária. A versao 1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# Saque- O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de extrato
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
# 1500.45 = R$ 1500.45


saldo = 0
limite_por_saque = 500
SAQUE_DIARIO = 3
total_saques = 0
extrato = ''
menu_principal = ''''
Seja Bem Vindo ao Gabi's Bank!\n
Selecione uma das opções abaixo para prosseguirmos com o seu atendimento:\n
1. Depósito
2. Saque
3. Extrato Bancário
4. Sair\n
'''
while True:
    opcao_usuario = input(menu_principal)

    if opcao_usuario == '1':
        valor_a_ser_depositado = float(input('Qual valor você deseja depositar?\n'))
        if valor_a_ser_depositado > 0:
            saldo = saldo + valor_a_ser_depositado
            extrato = extrato + f'Depósito: R$ {valor_a_ser_depositado:.2f}\n'
            print('Valor depositado com sucesso!')
        else:
            print('Valor inválido para depósito.')
    elif opcao_usuario == '2':
        valor_a_ser_sacado = float(input('Qual valor deseja sacar?\n'))
        if valor_a_ser_sacado > saldo:
            print('Valor para saque insuficiente.')
        elif valor_a_ser_sacado > limite_por_saque:
            print('O valor a ser sacado ultrapassou o limite diário.')
        elif total_saques >= SAQUE_DIARIO:
            print('Limite de saques diários atingido.')
        else:
            saldo = saldo - valor_a_ser_sacado
            total_saques = total_saques + 1
            extrato = extrato + f'Saque: R$ {valor_a_ser_sacado:.2f}\n'
            print('Valor sacado com sucesso!')
    elif opcao_usuario == '3':
        print('################ EXTRATO ################')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('#########################################')
    elif opcao_usuario == '4':
        break
    else:
        print('Opção inválida. Por gentileza, selecione a opção desejada.')
    

