from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "pensar"
print("\033[1;36m -=+=- \033[m" * 20)
print('\033[0;37m Vou pensar em um numero entre 0 e 5 \033[m...')
print("Pensando...")
sleep(3)
print("\033[1;36m -=+=- \033[m" * 20)
jogador = int(input('\033[0;37m Em que numero você acha que eu pensei? \033[m')) # o jogador tenta adivinhar
print("Vamos ver...")
sleep(3)
print("\033[1;32;47m ACERTOU!! \033[m" if jogador == computador else "\033[1;31;47m Você errou! \033[m\nO numero era \033[34m{}\033[m, não \033[31m{}\033[m".format(computador, jogador))
