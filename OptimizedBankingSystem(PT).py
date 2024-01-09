
def menu():

    menu = input("""
Escolha uma opção:

Se deseja Sacar -> Digite [S]
Se deseja Depositar -> Digite [D]
Se deseja acessar o Extrato -> Digite [E]
Se deseja Criar um novo usuário -> Digite [U]
Se deseja Cria uma nova conta -> Digite [C]
Se deseja Ver as contas existentes -> Digite [V]
Para sair -> Digite [Q]

> """).upper()

    return menu

def templete(y):
    x = ""
    x += y
    logo1 = " Banco Python "
    print()
    print(logo1.center(80,'+'))
    print()
    print(x.center(80))
    print()
    print("".center(80,'+'))
    print()
    print()

def deposito(extrato, saldo, /):
    while True:
        try:
            print()
            print("Opção -> Depósito\n")
            deposito = float(input("""
Informe o valor do depósito:
                                                   
Caso deseje voltar para o menu inicial, 
escreva qualquer letra e tecle Enter.
                                                   
>"""))
                            


            if deposito >= 0:
                saldo += deposito
                extrato += f"+R${deposito:.2f}\n"
                templete(f"""
    Depósito de R${deposito:.2f} efetuado.
    Saldo atual: R${saldo:.2f}""")
                break
            else:
                print("""
    Valor incorreto. 
    Tente um valor numérico positivo.
    Exemplo: 50.00""")
                                
        except ValueError:
            break

    return extrato, saldo
    
def saque(*, limite, saldo, extrato):

    if limite ==0:
        templete("Você já chegou no limite de saques diários (3 por dia)")

    elif saldo == 0:
        templete("Você não possui dinheiro para sacar")

    elif saldo > 0 and limite > 0:
        while True:
            try:
                print()
                print("Opção -> Saque\n")
                saque = float(input("""
Quanto deseja sacar? 
                                                    
Caso deseje voltar para o menu inicial, 
escreva qualquer letra e tecle Enter. 
                                                    
>"""))

                if saque > 500:
                    templete("Saque no máximo de R$500.00")

                elif saque <= 0:
                    templete("O valor do saque precisa ser maior que R$ 0,00")

                elif (saque > 0) and (saldo < saque):
                    templete("Boa tentativa.")

                elif (saque > 0) and (saldo >=saque):
                    saldo -= saque
                    extrato += f"-R${saque:.2f}\n"
                    limite -= 1

                    templete(f"""
Saque de R${saque:.2f} efetuado. 
Saldo atual: R${saldo:.2f}""")
                    
                    break

            except ValueError:
                break
                    
    return (limite, saldo, extrato)

def extrato_f(extrato, saldo):

    if extrato == "":
        templete("""
                        EXTRATO

                        R$ 0,00
                                 """)

    else:
        templete(f"""
Opção -> Extrato:
                                 
{extrato}

Saldo total de: R${saldo:.2f}""")

def novo_user(user):

    templete("Opção -> registro de novo usuário através do CPF\n")
    try:
        cpf = int(input("Qual é o seu CPF?\n>"))
        usuario = filtro(cpf, user)

        

        if usuario:
            templete("CPF já cadastrado")
            return

        else:
            nome = input("Qual seu nome completo?\n>")
            data = input("Qual a sua data de nascimento? DD-MM-AAAA\n>")
            endereco = input("Qual seu endereço?\nLogradourao, número, bairro, cidade, estado\n>")


            user.append({"nome":nome, "data":data, "cpf":cpf, "endereco":endereco})
            templete("CPF registrado com sucesso")
            
    
    except ValueError:
        templete("CPF precisa ser um número")
        
def filtro(cpf, user):
    teste = [x for x in user if cpf in x.values()]
    return teste[0] if teste else None
    
def nova_conta(user, AGENCIA, lista_contas, n_contas):

    templete("Opção -> criar uma nova conta através do CPF\n")
    try:
        cpf = int(input("Qual é o seu CPF?\n>"))
        usuario = filtro(cpf, user)

        if usuario:
            
            nome1 = input("Favor digitar o nome da pessoa que irá utilizar essa conta\n>")
            n_contas += 1
            templete(f"""
    Conta de: {nome1}
    Número da conta = {str(n_contas).zfill(4)}
    Agência = {AGENCIA}
    CPF cadastrado = {cpf}

    """)
            lista_contas += f"""
    Conta de: {nome1}
    Número da conta = {str(n_contas).zfill(4)}
    Agência = {AGENCIA}
    CPF cadastrado = {cpf}

    """
            
            return lista_contas, n_contas
    
        else:
            templete("É necessário primeiro criar um novo usuário para cadastrar o CPF")
            return lista_contas, n_contas

    except ValueError:
        templete("CPF precisa ser um número")
        return lista_contas, n_contas

def cadastros(lista_contas):

    if lista_contas == "":
        templete("Nenhuma conta criada por enquanto")

    else:
        templete(f"""
                Opção -> Mostrando cadastros existentes.

{lista_contas}                                 
""")
        
def sair():
    templete("""
                                Obrigado por vir. 
                        Seu Dinheiro está seguro conosco. 
                                 Volte sempre.""")

def main():

    
    extrato = ""
    saldo = 0
    limite = 3
    user = []
    AGENCIA = "0001"
    lista_contas = ""
    n_contas = 0

    templete("Nós do banco Python lhe damos boas-vindas ao banco dos seu $onho$ !")

    while True:


        
    

        opc = menu()

        if opc == "D":

            extrato, saldo = deposito(extrato, saldo)

        elif opc == "S":

            limite, saldo, extrato = saque(limite=limite, saldo=saldo, extrato=extrato)

        elif opc == "Q":

            sair()
            break

        elif opc == "E":

            extrato_f(extrato, saldo)

        elif opc == "U":

            novo_user(user)

        elif opc == "C":

            lista_contas, n_contas = nova_conta(user, AGENCIA, lista_contas, n_contas)


        elif opc == "V":

            cadastros(lista_contas)       

        

        else:
            templete("Opção invalida. Favor se atentar ao Menu de opções")
    
main()