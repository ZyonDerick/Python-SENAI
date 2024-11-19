print("Bem-vindo ao Jokenpô")
print("-"*50)
print("Escolha uma das opções disponíveis\nPEDRA\nPAPEL\nTESOURA")
print("-"*50)

player1 = input("Player 1 Digite sua escolha: ").upper()
player2 = input("Player 2 Digite sua escolha: ").upper()

"""
if (player1 == player2):
    print(f"Player 1 jogou {player1} e Player 2 jogou {player2}: EMPATE")
elif (player1 == "PEDRA") and (player2 != "TESOURA"):
    print(f"Player 1 jogou {player1} \nPlayer 2 jogou {player2}\nPlayer 2 ({player2}) ganhou!")
elif (player1 == "TESOURA") and (player2 != "PAPEL"):
    print(f"Player 1 jogou {player1} \nPlayer 2 jogou {player2}\nPlayer 2 ({player2}) ganhou!")
elif (player1 == "PAPEL") and (player2 != "PEDRA"):
    print(f"Player 1 jogou {player1} \nPlayer 2 jogou {player2}\nPlayer 2 ({player2}) ganhou!")
elif (player1 != "PEDRA" or player1 != "PAPEL" or player1 != "TESOURA") or (player2 != "PEDRA" or player1 != "PAPEL" or player1 != "TESOURA"):
    print("Jogada inválida!")
else:
    print(f"Player 1 jogou {player1} \nPlayer 2 jogou {player2}\nPlayer 1 ({player1}) ganhou!")
"""

if (player1 == "PEDRA" and player2 == "TESOURA") or (player1 == "TESOURA" and player2 == "PAPEL") or (player1 == "PAPEL" and player2 == "PEDRA"):
    print("Player 1 ganhou!")
elif (player1 == "TESOURA" and player2 == "PEDRA") or (player1 == "PAPEL" and player2 == "TESOURA") or (player1 == "PEDRA" and player2 == "PAPEL"):
    print("Player 2 ganhou!")
elif player1 == player2:
    print("Empate!")
else:
    print("Jogada inválida!")