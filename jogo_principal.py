from random import randint
jogadas = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']
jogada_pc = randint(0, 4)
print('-=' * 25)
print(
    '1 - Pedra\n'
    '2 - Papel\n'
    '3 - Tesoura\n'
    '4 - Lagarto\n' 
    '5 - Spock'
)
print('-=' * 25)
jogada_usario = int(input('Digite sua jogada: '))
jogada_usario = jogada_usario - 1
print('-=' * 25)
print(
    f'Jogador escolheu: {jogadas[jogada_usario]}\n'
    f'PC escolheu: {jogadas[jogada_pc]}'
)
print('-=' * 25)
if jogada_pc == 0:
    if jogada_usario in (3, 2):
        print('PC ganhou')
    elif jogada_usario == 0:
        print('Empate')
    else:
        print('Jogador ganhou')
elif jogada_pc == 1:
    if jogada_usario in (0, 4):
        print('PC ganhou')
    elif jogada_usario == 1:
        print('Empate')
    else:
        print('Jogador ganhou')
elif jogada_pc == 2:
    if jogada_usario in (1, 3):
        print('PC ganhou')
    elif jogada_usario == 2:
        print('Empate')
    else:
        print('Jogador ganhou')
elif jogada_pc == 3:
    if jogada_usario in (4, 1):
        print('PC ganhou')
    elif jogada_usario == 3:
        print('Empate')
    else:
        print('Jogador ganhou')
elif jogada_pc == 4:
    if jogada_usario in (0, 2):
        print('PC ganhou')
    elif jogada_usario == 4:
        print('Empate')
    else:
        print('Jogador ganhou')
