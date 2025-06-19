import random
#Desenvolvendo um Jogo de Pedra, Papel e Tesoura!
# \033[m - Terminal de Cores


palavras = ['Pedra', 'Papel', 'Tesoura']
escolhidas = random.choice(palavras)

jogar = input('''\033[34mVamos Jogar! 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Escolha a Numeração de uma das Opções: \033[m''')
if jogar == '0':
    print('Você Jogou Pedra!')
    joga = 'Pedra'
    if joga == escolhidas:
        print('Empate!!!')
    elif escolhidas == 'Papel':
        print('Ala! Você Perdeu!')
    elif escolhidas == 'Tesoura':
        print('Parabens, Você Ganhou!')

if jogar == '1':
    print('Você Jogou Papel!')
    joga = 'Papel'
    if joga == escolhidas:
        print('Empate!!!')
    elif escolhidas == 'Tesoura':
        print('Ala! Você Perdeu!')
    elif escolhidas == 'Pedra':
        print('Parabens, Você Ganhou!')

if jogar == '2':
    print('Você Jogou Tesoura!')
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