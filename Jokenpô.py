import random #Biblioteca de Sorteio/Gerador de Número
from time import sleep # Biblioteca de tempo

#Desenvolvendo um Jogo de Pedra, Papel e Tesoura!
# \033[m - Terminal de Cores

#Fazendo o Sorteio das Palavras
palavras = ['Pedra', 'Papel', 'Tesoura']
escolhidas = random.choice(palavras)

#Pedindo para o Usuario escolher uma Opção
jogar = input('''\033[34mVamos Jogar! 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Escolha a Numeração de uma das Opções: \033[m''')

#Usando a Biblioteca time para efeitos dentro do código/jogo
print('\033[31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\033[m')
sleep(1)
print('\033[32m=' * 50)

#Usando Condições Aninhadas para estruturar o código
if jogar == '0':
    print('\033[32mVocê Jogou Pedra!')
    print(f'O Computador Jogou {escolhidas}!\033[m')
    print('\033[36m=' * 50)
    joga = 'Pedra'
    if joga == escolhidas:
        print('Empate!!!')
    elif escolhidas == 'Papel':
        print('Ala! Você Perdeu!')
    elif escolhidas == 'Tesoura':
        print('Parabens, Você Ganhou!')

elif jogar == '1':
    print('\033[32mVocê Jogou Papel!')
    print(f'O Computador Jogou {escolhidas}!\033[m')
    print('\033[36m=' * 50)
    joga = 'Papel'
    if joga == escolhidas:
        print('Empate!!!')
    elif escolhidas == 'Tesoura':
        print('Ala! Você Perdeu!')
    elif escolhidas == 'Pedra':
        print('Parabens, Você Ganhou!')

elif jogar == '2':
    print('\033[32mVocê Jogou Tesoura!')
    print(f'O Computador Jogou {escolhidas}!\033[m')
    print('\033[36m=' * 50)
    joga = 'Tesoura'
    if joga == escolhidas:
        print('Empate!!!')
    elif escolhidas == 'Pedra':
        print('Ala! Você Perdeu!')
    elif escolhidas == 'Papel':
        print('Parabens, Você Ganhou!')

else:
    print('Opção Invalida!')

print('Obrigado Por Jogar!')