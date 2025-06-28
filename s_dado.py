import random
input("Pressione ENTER para jogar: ")

jogador1 = random.randint(1,6)
print(f"Jogador 1 rolou o número {jogador1}")

jogador2 = random.randint(1,6)
print(f"Jogador 2 rolou o número {jogador2}")

if jogador1 >jogador2:
    print("Jogador 1 ganhou")
elif jogador2 > jogador1:
    print("Jogador 2 ganhou")
else:
    print("Empate! Rolem os dados de novo!")
    