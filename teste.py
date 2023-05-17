import random

print("Bem-vindo ao jogo de pedra, papel e tesoura!")
jg1 = input("Insira o nome do jogador 1: ")
jg2 = input("Insira o nome do jogador 2: ")

pergunta = str(input('Deseja jogar? [s/n]')).lower()

while pergunta == 's':
    quantidade_de_rodadas = int(input('Quantas rodadas vocês pretendem jogar? '))
    a = 0
    p1 = 0
    p2 = 0

    while a < quantidade_de_rodadas:
        print(f"\nRodada {a+1}")
        lista1 = ['pedra', 'papel', 'tesoura']
        lista2 = ['pedra', 'papel', 'tesoura']
        esc1 = random.choice(lista1)
        esc2 = random.choice(lista2)
       

        if esc1 == esc2:
            print("Empate!")
        elif (esc1 == "pedra" and esc2 == "tesoura") or (esc1 == "papel" and esc2 == "pedra") or (esc1 == "tesoura" and esc2 == "papel"):
            print(f"{jg1} ganhou a rodada!{jg1} escolheu {esc1} e {jg2} escolheu {esc2}\n{esc1} ganaha de {esc2}")
            p1 += 1
        else:
            print(f"{jg2} ganhou a rodada!{jg2} escolheu {esc2} e {jg1} escolheu {esc1}\n{esc2} ganaha de {esc1}")
            p2 += 1

        a += 1

    if p1 > p2:
        print(f"\n{jg1} ganhou o jogo por {p1} a {p2}!")
    elif p2 > p1:
        print(f"\n{jg2} ganhou o jogo por {p2} a {p1}!")
    else:
        print(f"\nO jogo terminou empatado por {p1} a {p2}!")

    pergunta = str(input('\nDesejam jogar novamente? [s/n]')).lower()

print('\n===== Até a próxima!=====')  