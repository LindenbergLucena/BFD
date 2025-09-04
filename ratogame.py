import random

print("""Bem vindo a caça ao queijo""")

lugares = ["ratoeira","geladeira","fogao","banheiro","guarda_roupa","mesa","quarto","garagem","pia"]

local_aleatorio = random.randint(1, 9)

encontrou = False
tentativas = 0

print("Você tem 3 tentativas)")

while tentativas < 3:
    local_queijo = int(input(f"Tentativa {tentativas + 1}/3 - Escolha um local de 1 a 9: "))

    if local_queijo == local_aleatorio:
        print("O rato encontrou o queijo, parabéns!!!")
        encontrou = True
        break
    else:
        print("O rato não encontrou o queijo, tente novamente!!!")

    tentativas += 1
    nome_local_queijo = lugares[local_aleatorio - 1]

if not encontrou:
    print("\nSuas tentativas acabaram!")

print(f"O queijo estava no(a): {local_aleatorio}  {nome_local_queijo}")
