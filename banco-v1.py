"""Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o 
usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível 
sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos 
na operação de extrato.

Extrato: deve listar todos os depósitos e saques realizados. No fim da listagem, deve ser exibido o 
saldo atual da conta (R$ XXX.XX)."""

# Dados da conta
saldo = 1000  # Valor do saldo inicial
limite = 500  # Limite máximo de saque por operação
numero_saques = 0  # Número de saques realizados
limite_saque = 3  # Limite diário de saques

# Menu do banco
print('Bem vindo ao Banco X!')
print('s - Saque; \nd - Depósito; \ne - Extrato; \nq - Sair.')

# Início do programa
while True:
    op = input(str('Qual a opção? ')).lower()

# Operações do banco

# Saque
    if op == 's':
        if numero_saques < limite_saque:
            valor_saque = input('Qual valor deseja sacar? R$ ')
            valor_saque = float(valor_saque)

            if valor_saque > limite:
                print('Infelizmente, você só poderá sacar R$ 500,00.')

            elif valor_saque < 0:
                print('Não é possível sacar valor negativo.')

            elif numero_saques < limite_saque and valor_saque < saldo and valor_saque <= limite:
                print(saldo)
                numero_saques = numero_saques + 1
                saldo = saldo - valor_saque
                print(f'Você sacou R$ {valor_saque:.2f}. Seu saldo é de R$ {saldo:.2f}.')

            elif numero_saques >= limite_saque:
                print('Você já realizou o limite de saques diários.')

            else:
                print('Você não possui saldo em conta para essa operação')

# Depósito
    elif op == 'd':
        valor_deposito = float(input('Qual o valor de depósito? R$ '))

        if valor_deposito < 0:
            print('Não é possível depositar valor negativo!')

        else:
            saldo = saldo + valor_deposito  
            print(f'Valor atual do saldo: R$ {saldo:.2f}')  

# Extrato
    elif op == 'e':
        print('==========EXTRATO==========')
        print(f'Saldo em conta: R$ {saldo:.2f}')
        print('============================')

# Sair
    elif op == 'q':
        print('Tenha um ótimo dia!')
        break

# Outra opção
    else:
        print('Essa opção não existe. Selecione uma operação válida.')