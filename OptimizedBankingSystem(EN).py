
def menu():

    menu = input("""
Choose an option:

If you want to Withdraw -> Type [W]
If you want to Deposit -> Type [D]
If you want to access the Statement -> Type [S]
If you want to create a new User -> Type [U]
If you want to Create a new account -> Type [C]
If you want to View existing accounts -> Type [V]
To Quit -> Type [Q]

> """).upper()

    return menu

def templete(y):
    x = ""
    x += y
    logo1 = " Python Bank "
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
            print("Option -> Deposit\n")
            deposito = float(input("""
                                   
Enter the deposit amount:

If you wish to return to the main menu,
type any letter and press Enter.
                                                   
>"""))
                            


            if deposito >= 0:
                saldo += deposito
                extrato += f"+${deposito:.2f}\n"
                templete(f"""
    Deposit of ${deposito:.2f} made.
    Current balance: ${saldo:.2f}""")
                break
            else:
                print("""
Incorrect value.
Try a positive numerical value.
Example: 50.00""")
                                
        except ValueError:
            break

    return extrato, saldo
    
def saque(*, limite, saldo, extrato):

    if limite ==0:
        templete("You have reached the daily withdrawal limit (3 per day).")

    elif saldo == 0:
        templete("You do not have sufficient funds to withdraw.")

    elif saldo > 0 and limite > 0:
        while True:
            try:
                print()
                print("Option -> Withdrawal\n")
                saque = float(input("""
How much do you want to withdraw?

If you wish to return to the main menu,
type any letter and press Enter. 
                                                    
>"""))

                if saque > 500:
                    templete("Withdraw up to $ 500.00 at most.")

                elif saque <= 0:
                    templete("The withdrawal amount needs to be greater than $ 0.00.")

                elif (saque > 0) and (saldo < saque):
                    templete("Nice try.")

                elif (saque > 0) and (saldo >=saque):
                    saldo -= saque
                    extrato += f"-R${saque:.2f}\n"
                    limite -= 1

                    templete(f"""
Withdrawal of ${saque:.2f} made. 
Current balance: ${saldo:.2f}""")
                    
                    break

            except ValueError:
                break
                    
    return (limite, saldo, extrato)

def extrato_f(extrato, saldo):

    if extrato == "":
        templete("""
                        Balance

                        $ 0,00
                                 """)

    else:
        templete(f"""
Option -> Balance:
                                 
{extrato}

Total balance of: ${saldo:.2f}""")

def novo_user(user):

    templete("Option -> Register a new user using the ID\n")
    try:
        cpf = int(input("What is your ID?\n>"))
        usuario = filtro(cpf, user)

        

        if usuario:
            templete("ID already registered")
            return

        else:
            nome = input("What is your full name?\n>")
            data = input("What is your date of birth? MM-DD-YYYY\n>")
            endereco = input("What is your address?\nStreet, number, neighborhood, city, state\n>")


            user.append({"name":nome, "date":data, "ID":cpf, "adress":endereco})
            templete("ID successfully registered.")
            
    
    except ValueError:
        templete("ID must be a numerical value.")
        
def filtro(cpf, user):
    teste = [x for x in user if cpf in x.values()]
    return teste[0] if teste else None
    
def nova_conta(user, AGENCIA, lista_contas, n_contas):

    templete("Option -> Create a new account using the ID\n")
    try:
        cpf = int(input("What is your ID?\n>"))
        usuario = filtro(cpf, user)

        if usuario:
            
            nome1 = input("Please enter the name of the person who will use this account.\n>")
            n_contas += 1
            templete(f"""
    Account for: {nome1}
    Account number = {str(n_contas).zfill(4)}
    Branch = {AGENCIA}
    Registered ID = {cpf}

    """)
            lista_contas += f"""
    Account for: {nome1}
    Account number = {str(n_contas).zfill(4)}
    Branch = {AGENCIA}
    Registered ID = {cpf}

    """
            
            return lista_contas, n_contas
    
        else:
            templete("It is necessary to first create a new user to register the ID.")
            return lista_contas, n_contas

    except ValueError:
        templete("ID must be a numerical value.")
        return lista_contas, n_contas

def cadastros(lista_contas):

    if lista_contas == "":
        templete("No accounts created so far.")

    else:
        templete(f"""
                Option -> Displaying existing registrations.

{lista_contas}                                 
""")
        
def sair():
    templete("""
                                Thank you for coming.
                             Your money is safe with us.
                         We look forward to your next visit.""")

def main():

    
    extrato = ""
    saldo = 0
    limite = 3
    user = []
    AGENCIA = "0001"
    lista_contas = ""
    n_contas = 0

    templete("We at Python Bank welcome you to the bank of your dream$ !")

    while True:


        
    

        opc = menu()

        if opc == "D":

            extrato, saldo = deposito(extrato, saldo)

        elif opc == "W":

            limite, saldo, extrato = saque(limite=limite, saldo=saldo, extrato=extrato)

        elif opc == "Q":

            sair()
            break

        elif opc == "S":

            extrato_f(extrato, saldo)

        elif opc == "U":

            novo_user(user)

        elif opc == "C":

            lista_contas, n_contas = nova_conta(user, AGENCIA, lista_contas, n_contas)


        elif opc == "V":

            cadastros(lista_contas)       

        

        else:
            templete("Invalid option. Please pay attention to the menu of options.")
    
main()