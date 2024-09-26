import os
os.system("cls||clear")

# Valores dos pratos
valor_1 = 15.00
valor_2 = 20.00

# Cardápio
print("= CARDÁPIO DO DIA =")
print(""""
       código = 123 - Morango
       código = 244 - Chocolate
       código = 357 - Leite Ninho
       código = 424 - Abacaxi
       código = 556 - Melancia
       código = 656 - Ninho trufado
       código = 789 - Chocolate alpino
""")

prato = int(input("Digite o número do prato escolhido: "))

def calcular_total(valor, forma_pagamento):
    if forma_pagamento == 1:  # À Vista
        return valor * 0.90  # 10% desconto
    elif forma_pagamento == 2:  # Cartão de Crédito
        return valor


if prato == 123:
    forma_pagamento = int(input("Escolha a forma de pagamento:\n1- À Vista\n2- Cartão de Crédito\nDigite: "))
    total = calcular_total(valor_1, forma_pagamento)
    print(f"Total: R${total:.2f}")

elif prato == 244:
    forma_pagamento = int(input("Escolha a forma de pagamento:\n1- À Vista\n2- Cartão de Crédito\nDigite: "))
    total = calcular_total(valor_2, forma_pagamento)
    print(f"Total: R${total:.2f}")

while True:
    solicitacao_prato = input("Deseja mais geladinho? (s/n): ").strip().lower()
    
    if solicitacao_prato == "s":
        prato = int(input("Digite o código do prato: "))
        forma_pagamento = int(input("Escolha a forma de pagamento:\n1- À Vista\n2- Cartão de Crédito\nDigite: "))
        
        if prato == 123:
            total += calcular_total(valor_1, forma_pagamento)
        elif prato == 244:
            total += calcular_total(valor_2, forma_pagamento)
     
        print(f"Total acumulado: R${total:.2f}")
    
    elif solicitacao_prato == "n":
        print(f"Seu pedido foi finalizado. Total final: R${total:.2f}")
        break
    else:
        print("Opção inválida. Por favor, digite 's' ou 'n'.")

