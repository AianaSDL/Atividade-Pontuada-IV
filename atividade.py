import os
os.system("cls||clear")

valor_1 = 15
valor_2 = 20

print("= CARDÁPIO DO DIA =")
print (""""
    código = 1 - Morango
    código = 2 - Chololate
    código = 3 - Leite Ninho
    código = 4- Abacaxi
    código = 5- Melancia
    código = 6 - Ninho trufado
    código = 7- Chocolate alpino
     """)

prato = int(input("Digite o numero do prato escolhido: "))


while True:
    prato = 1
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
      
  
            
    prato= 2
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
        
    

    prato= 3
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
    
  
    
    
    prato= 4
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
       
  
    

    prato= 5
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
       
  
    prato= 6
    pagamento = float(input("Digite a forma de pagamento: "))
    print ("""
    1- A Vista
    2- Cartão de Credito""")

    prato= 6
    pagamento = float(input("Digite a forma de pagamento: "))
    print ("""
    1- A Vista
    2- Cartão de Credito""")

    prato = 0
    print("Codigo invalido")
    print(input("Digite o codigo novamente: "))
    
     
