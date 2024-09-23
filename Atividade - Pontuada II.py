import os
os.system("cls | clear")

print("= CARDÁPIO DO DIA =")

codigo_salvo = int(input(""""
    código = 123 - Morango
    código = 244 - Chololate
    código = 357 - Leite Ninho
    código = 424 - Abacaxi
    código = 556 - Melancia
    código = 656 - Ninho trufado
    código = 789 - Chocolate alpino
     """))

prato = int(input("Digite o numero do prato escolhido: "))

while True:
    codigo = int(input("Digite o código do menu"))
    if codigo - codigo_salvo:
        print("Código inválido, Digite o código novamente: ")
        break
   
