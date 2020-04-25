from random import randint
from time import sleep
from os import system

jogadas = ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']
mensagens = [
    'Tesoura corta papel',
    'Papel cobre pedra',
    'Pedra esmaga lagarto',
    'Lagarto envenena Spock',
    'Spock quebra tesoura',
    'Tesoura decapita lagarto',
    'Lagarto come papel',
    'Papel refuta Spock',
    'Spock vaporiza pedra',
    'Pedra amassa tesoura'
]
jogada_pc = randint(0, 4)
jogada_usuario_var = 0


def limpa_tela():
    system('cls')


def instrucoes():
    print(
        '\nEste jogo é um aprimoramento do clássico jogo pedra, papel e tesoura, pois dessa forma as chances de empate '
        'diminuem\n'
        'A ordem de quem ganha de quem é a seguinte: \n'
    )
    for mensagem_atual in mensagens:
        print(mensagem_atual)
    print()


def menu():
    while True:
        print('-=' * 25)
        print(
            '1 - Iniciar o jogo\n'
            '2 - Instruções\n'
            '3 - Sair'
        )
        print('-=' * 25)
        escolha_menu = input('Digite sua escolha: ')
        if escolha_menu == '1':
            break
        elif escolha_menu == '2':
            instrucoes()
        elif escolha_menu == '3':
            exit()
        else:
            print('Escolha uma opção válida.')


def jogada_usuario():
    global jogada_usuario_var
    while True:
        jogada_usuario_var = input('Digite sua jogada: ')
        if jogada_usuario_var not in ('1', '2', '3', '4', '5'):
            print('Digite uma opção válida')
        else:
            jogada_usuario_var = int(jogada_usuario_var) - 1
            break


while True:
    limpa_tela()
    menu()
    print('-=' * 25)
    print(
        '1 - Pedra\n'
        '2 - Papel\n'
        '3 - Tesoura\n'
        '4 - Lagarto\n'
        '5 - Spock'
    )
    print('-=' * 25)
    jogada_usuario()
    print('-=' * 25)
    print(
        f'\nJogador escolheu: {jogadas[jogada_usuario_var]}\n'
        f'PC escolheu: {jogadas[jogada_pc]}\n'
    )
    print('-=' * 25)
    sleep(1)
    print()
    if jogada_pc == 0:
        if jogada_usuario_var in (3, 2):
            if jogada_usuario_var == 2:
                print(mensagens[9])
            if jogada_usuario_var == 3:
                print(mensagens[2])
            print('PC ganhou')
        elif jogada_usuario_var == 0:
            print('Empate')
        if jogada_usuario_var in (1, 4):
            if jogada_usuario_var == 1:
                print(mensagens[1])
            if jogada_usuario_var == 4:
                print(mensagens[8])
            print('Jogador ganhou')
    elif jogada_pc == 1:
        if jogada_usuario_var in (0, 4):
            if jogada_usuario_var == 0:
                print(mensagens[1])
            if jogada_usuario_var == 4:
                print(mensagens[7])
            print('PC ganhou')
        elif jogada_usuario_var == 1:
            print('Empate')
        if jogada_usuario_var in (2, 3):
            if jogada_usuario_var == 2:
                print(mensagens[0])
            if jogada_usuario_var == 3:
                print(mensagens[6])
            print('Jogador ganhou')
    elif jogada_pc == 2:
        if jogada_usuario_var in (1, 3):
            if jogada_usuario_var == 1:
                print(mensagens[0])
            if jogada_usuario_var == 3:
                print(mensagens[5])
            print('PC ganhou')
        elif jogada_usuario_var == 2:
            print('Empate')
        if jogada_usuario_var in (0, 4):
            if jogada_usuario_var == 0:
                print(mensagens[9])
            if jogada_usuario_var == 4:
                print(mensagens[4])
            print('Jogador ganhou')
    elif jogada_pc == 3:
        if jogada_usuario_var in (4, 1):
            if jogada_usuario_var == 1:
                print(mensagens[6])
            if jogada_usuario_var == 4:
                print(mensagens[3])
            print('PC ganhou')
        elif jogada_usuario_var == 3:
            print('Empate')
        if jogada_usuario_var in (0, 2):
            if jogada_usuario_var == 0:
                print(mensagens[2])
            if jogada_usuario_var == 2:
                print(mensagens[5])
            print('Jogador ganhou')
    elif jogada_pc == 4:
        if jogada_usuario_var in (0, 2):
            if jogada_usuario_var == 0:
                print(mensagens[8])
            if jogada_usuario_var == 2:
                print(mensagens[4])
            print('PC ganhou')
        elif jogada_usuario_var == 4:
            print('Empate')
        if jogada_usuario_var in (1, 3):
            if jogada_usuario_var == 1:
                print(mensagens[7])
            if jogada_usuario_var == 3:
                print(mensagens[3])
            print('Jogador ganhou')
    print()
    print('-=' * 25)
    input('\nPressione enter para continuar')

