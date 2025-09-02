import random

print("""Bem vindo ao Jogo do Bicho 🐊 🦓 🐎
Aqui todos os seus sonhos são valorizados!""")

lista_bicho = ["Avestruz", "Águia", "Burro", "Borboleta", "Cachorro", 
               "Cabra", "Carneiro", "Camelo", "Cobra", "Coelho", 
               "Cavalo", "Elefante", "Galo", "Gato", "Jacaré", 
               "Leão", "Macaco", "Porco", "Pavão", "Peru", 
               "Touro", "Tigre", "Urso", "Veado", "Vaca"]

bicho_sorteado_numero = random.randint(1, 25)

tentativas = 0
acertou = False 
print("Você tem 5 tentativas.")

while tentativas < 5:
    
    bicho_escolhido = int(input(f"Tentativa {tentativas + 1}/5 - Escolha um bicho de 1 a 25: "))

    if bicho_escolhido == bicho_sorteado_numero:
        print("Parabéns, você acertou! Você é o cara! 😎")
        acertou = True 
        break 
    else:
        print("Você errou, tente novamente.")

    tentativas += 1
    nome_bicho_sorteado = lista_bicho[bicho_sorteado_numero - 1]


if not acertou:
    print("\nSuas tentativas acabaram!")

print(f"O bicho sorteado foi o número: {bicho_sorteado_numero}  {nome_bicho_sorteado}")