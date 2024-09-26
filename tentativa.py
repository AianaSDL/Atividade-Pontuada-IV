import os
os.system("cls||clear")
valor_1 = 15.00
valor_2 = 20.00
print("= CARDÁPIO DO DIA =")
print (""""
    código = 1 - Morango
    código = 2 - Chololate
    código = 3 - Leite Ninho
    código = 4 - Abacaxi
    código = 5 - Melancia
    código = 6 - Ninho trufado
    código = 7 - Chocolate alpino
     """)

prato = int(input("Digite o numero do prato escolhido: "))



match (prato):
    case 1:
        credito = valor_1 * 0.10
        vista = valor_1 + 0.10
        print ("""1- A Vista
        2- Cartão de Credito""")
        pagamento = int(input("Digite a forma de pagamento: "))
        if pagamento == 2:
           credito = print(f"Total: {credito}")
        elif pagamento == 1:
            vista = print(f"Total: {vista}")
    
    case 2:
        credito = valor_1 * 0.10
        vista = valor_1 + 0.10
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")

    case 3:
        credito = valor_1 * 0.10
        vista = valor_1 + 0.10
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")

    case 4:
        credito = valor_1 * 0.10
        vista = valor_1 + 0.10
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_1 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_1 + 0.10
            print(f"Total: {total}")
        
    case 5:
        credito = valor_2 * 0.10
        vista = valor_2 + 0.10
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_2 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_2 + 0.10
            print(f"Total: {total}")

    case 6:
        credito = valor_2 * 0.10
        vista = valor_2 + 0.10
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_2 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_2 + 0.10
            print(f"Total: {total}")

    case 7:
        credito = valor_2 * 0.10
        vista = valor_2 + 0.10
        pagamento = float(input("Digite a forma de pagamento: "))
        print ("""1- A Vista
            2- Cartão de Credito""")
        if pagamento == 1:
            total = valor_2 * 0.10
            print(f"Total: {total}")
        elif pagamento == 2:
            total = valor_2 + 0.10
            print(f"Total: {total}")
    case _:
        print("Opção invalida:")
        (input("Digite o numero do prato escolhido: "))

while True:
    solicitacao_prato = str(input("Deseja mais geladinho (s/n): "))
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
            
