import os
os.system("cls||clear")
valor_1 = 15.00
valor_2 = 20.00
print("= CARDÁPIO DO DIA =")
print (""""
    código = 123 - Morango
    código = 244 - Chololate
    código = 357 - Leite Ninho
    código = 424 - Abacaxi
    código = 556 - Melancia
    código = 656 - Ninho trufado
    código = 789 - Chocolate alpino
     """)

prato = int(input("Digite o numero do prato escolhido: "))



match (prato):
    case 123:
        credito = valor_1 * 0.10
        vista = valor_1 + 0.10
        print ("""1- A Vista
        2- Cartão de Credito""")
        pagamento = int(input("Digite a forma de pagamento: "))
        if pagamento == 2:
           credito = print(f"Total: {credito}")
        elif pagamento == 1:
            vista = print(f"Total: {vista}")
    
    case 244:
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")

    case 244:
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")

    case 244:
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")
        
    case 244:
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")

    case 244:
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")

while True:
    solicitacao_prato = str(input("Deseja mais geladinho: "))
    if solicitacao_prato == "s":
        prato =print(input("Digite o codigo: "))
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            total_2 = (total+ valor_1) * 0.10
    elif solicitacao_prato == "n":
        break
            

