import os
os.system("cls||clear")

valor_1 = 15
valor_2 = 20

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


while True:
    prato = "123"
    print ("""
    1- A Vista
    2- Cartão de Credito""")
    pagamento = int(input("Digite a forma de pagamento: "))
    if pagamento == "1":
        total = valor_1 * 0.10
        print(f"Total: {total}")
    elif pagamento == "2":
        total = valor_1 + 0.10
        print(f"Total: {total}")
        break
  
            
    prato= "244"
    print ("""
    1- A Vista
    2- Cartão de Credito""")
    pagamento = int(input("Digite a forma de pagamento: "))
    if pagamento == "1":
        total = valor_1 * 0.10
        print(f"Total: {total}")
    elif pagamento == "2":
        total = valor_1 + 0.10
        print(f"Total: {total}")
        break
  
    

    prato= 357
    print ("""
    1- A Vista
    2- Cartão de Credito""")
    pagamento = int(input("Digite a forma de pagamento: "))
    if pagamento == 1:
        total = valor_1 * 0.10
        print(f"Total: {total}")
    
    elif pagamento == 2:
        total = valor_1 + 0.10
        print(f"Total: {total}")
    break
  
    
    
    prato= "424"
    print ("""
    1- A Vista
    2- Cartão de Credito""")
    pagamento = int(input("Digite a forma de pagamento: "))
    if pagamento == "1":
        total = valor_1 * 0.10
        print(f"Total: {total}")
        break
    elif pagamento == "2":
        total = valor_1 + 0.10
        print(f"Total: {total}")
        break
  
    

    prato= "556"
    print ("""
    1- A Vista
    2- Cartão de Credito""")
    pagamento = int(input("Digite a forma de pagamento: "))
    if pagamento == "1":
        total = valor_1 * 0.10
        print(f"Total: {total}")
        break
    elif pagamento == "2":
        total = valor_1 + 0.10
        print(f"Total: {total}")
        break
  
    prato= "656"
    pagamento = float(input("Digite a forma de pagamento: "))
    print ("""
    1- A Vista
    2- Cartão de Credito""")

    prato= "656"
    pagamento = float(input("Digite a forma de pagamento: "))
    print ("""
    1- A Vista
    2- Cartão de Credito""")

    prato = "0"
    print("Codigo invalido")
    print(input("Digite o codigo novamente: "))
    break
     

