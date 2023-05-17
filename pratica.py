import random

usuarios_registrados = []

pergunta = str(input('Deseja jogar ? [s/n]')).lower()
while pergunta == 's' :
    nome_usuario = input('Insira seu nome: ')
    if nome_usuario in usuarios_registrados:
        print("Bem-vindo de volta, {}!".format(nome_usuario))
    else:
        usuarios_registrados.append(nome_usuario)
        print("Bem-vindo(a) ao jogo, {}!".format(nome_usuario))
    quantidade_de_rodadas = int(input('Quantas rodadas você pretende jogar? '))
    a = 0
    while a < quantidade_de_rodadas:
        lista1 = ['pedra', 'papel', 'tesoura']
        lista2 = ['pedra', 'papel', 'tesoura']
        jogador1 = random.choice(lista1)
        jogador2 = random.choice(lista2)
        if jogador1 == 'pedra' and jogador2 =='tesoura':
            print('{} colocou {} e {} colocou {}\n{} ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2, nome_usuario))
        elif jogador1 == 'tesoura' and jogador2 =='pedra':
            print('{} colocou {} e {} colocou {}\nJogador 2 ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2))
        elif jogador1 == 'papel' and jogador2 =='tesoura':
            print('{} colocou {} e {} colocou {}\nJogador 2 ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2))
        elif jogador1 == 'tesoura' and jogador2 =='papel':
            print('{} colocou {} e {} colocou {}\n{} ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2, nome_usuario))
        elif jogador1 == 'pedra' and jogador2 =='papel':
            print('{} colocou {} e {} colocou {}\nJogador 2 ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2))
        elif jogador1 == 'papel' and jogador2 =='pedra':
            print('{} colocou {} e {} colocou {}\n{} ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2, nome_usuario))
        elif jogador1 == 'papel' and jogador2 =='tesoura':
            print('{} colocou {} e {} colocou {}\nJogador 2 ganhou!!!'.format(nome_usuario, jogador1, "Jogador 2", jogador2))
        elif (jogador1 == 'papel' and jogador2 == 'papel') or (jogador1 == 'pedra' and jogador2 == 'pedra') or (jogador1 == 'tesoura' and jogador2 == 'tesoura'):
            print('Empate!')
        else:
            print('Erro, fim de jogo')
        a = a + 1
    pergunta = str(input('Deseja jogar novamente? [s/n]')).lower()



    #########################################################################################################################################################################

    ###############################sem sorteio############################
print("Bem-vindo ao jogo de pedra, papel e tesoura!")
nome1 = input("Insira o nome do jogador 1: ")
nome2 = input("Insira o nome do jogador 2: ")

pergunta = str(input('Deseja jogar? [s/n]')).lower()

while pergunta == 's':
    quantidade_de_rodadas = int(input('Quantas rodadas vocês pretendem jogar? '))
    a = 0
    pontos1 = 0
    pontos2 = 0

    while a < quantidade_de_rodadas:
        print(f"\nRodada {a+1}")
        escolha1 = input(f"{nome1}, escolha entre pedra, papel ou tesoura: ").lower()
        escolha2 = input(f"{nome2}, escolha entre pedra, papel ou tesoura: ").lower()

        while escolha1 not in ["pedra", "papel", "tesoura"] or escolha2 not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            escolha1 = input(f"{nome1}, escolha entre pedra, papel ou tesoura: ").lower()
            escolha2 = input(f"{nome2}, escolha entre pedra, papel ou tesoura: ").lower()

        if escolha1 == escolha2:
            print("Empate!")
        elif (escolha1 == "pedra" and escolha2 == "tesoura") or (escolha1 == "papel" and escolha2 == "pedra") or (escolha1 == "tesoura" and escolha2 == "papel"):
            print(f"{nome1} ganhou a rodada! escolheu {escolha1} e {nome2} escolheu {escolha2}")
            pontos1 += 1
        else:
            print(f"{nome2} ganhou a rodada! escolheu {escolha2} e {nome1} escolheu {escolha1}")
            pontos2 += 1

        a += 1

    if pontos1 > pontos2:
        print(f"\n{nome1} ganhou o jogo por {pontos1} a {pontos2}!")
    elif pontos2 > pontos1:
        print(f"\n{nome2} ganhou o jogo por {pontos2} a {pontos1}!")
    else:
        print(f"\nO jogo terminou empatado por {pontos1} a {pontos2}!")

    pergunta = str(input('\nDesejam jogar novamente? [s/n]')).lower()

print('\n=====Valeu, pessoal! Até a próxima!=====')  

##############################################################################################################################################################################

###########################com srteio########################
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
#####################################################################################################################################################


from tkinter import *
from tkinter import ttk


cor1 = "#0D81DE"
cor2 = "#F57C23"
cor3 = "#DED914"
cor4 = "#E1F2B3"
cor5 = "#30151B"


area=Tk()
area.title('calculadora')
area.geometry('350x490')
area.config(bg=cor4)
frame_tela = Frame(area, width=350, height=120, bg= cor5)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(area, width=350, height=480, )
frame_corpo.grid(row=1, column=0)


tot_valores = ''
valor_texto = StringVar()

def Entrada_de_Valores(event):
    global tot_valores
    tot_valores = tot_valores +str( event)

    valor_texto.set(tot_valores)


def calcular():
    global tot_valores
    resultado= eval(tot_valores)
    print(resultado)
    valor_texto.set(resultado)

def limpar_tudo():
    global tot_valores
    tot_valores = ''
    valor_texto.set("")


tela_label = Label(frame_tela, width=16 , height=3, textvariable=valor_texto, font=('Ivy 27'), relief=FLAT , anchor= 'e', justify=RIGHT   , padx=7,bg=cor5,fg='white')
tela_label.place(x=0, y=0)

bot1 = Button(frame_corpo, command= lambda: Entrada_de_Valores('%'), text="%", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot1.place(x=0 , y=0)

bot2 = Button(frame_corpo, command= lambda: Entrada_de_Valores(''),text="₠", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot2.place(x=87, y=0)

bot3 = Button(frame_corpo, command= limpar_tudo,text="C", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot3.place(x=170, y=0)

bot4 = Button(frame_corpo, command= lambda: Entrada_de_Valores(''),text="◁", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot4.place(x=250, y=0)

bot5 = Button(frame_corpo, command= lambda: Entrada_de_Valores('1/χ"'),text="1/χ", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot5.place(x=0, y=60)

bot6 = Button(frame_corpo, command= lambda: Entrada_de_Valores('χ^2'),text="χ^2", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )

bot6.place(x=87, y=60)

bot7 = Button(frame_corpo, command= lambda: Entrada_de_Valores('√χ'),text="√χ", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot7.place(x=170 , y=60)

bot8 = Button(frame_corpo, command= lambda: Entrada_de_Valores('/'),text="÷", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot8.place(x=250, y=60)

bot9 = Button(frame_corpo, command= lambda: Entrada_de_Valores('7'),text="7", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot9.place(x=0, y=120)

bot10 = Button(frame_corpo, command= lambda: Entrada_de_Valores('8'),text="8", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot10.place(x=87, y=120)

bot11 = Button(frame_corpo, command= lambda: Entrada_de_Valores('9'),text="9", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot11.place(x=170, y=120)

bot12 = Button(frame_corpo, command= lambda: Entrada_de_Valores('*'),text="x", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot12.place(x=250, y=120)

bot13 = Button(frame_corpo, command= lambda: Entrada_de_Valores('4'),text="4", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot13.place(x=0, y=180)

bot14 = Button(frame_corpo, command= lambda: Entrada_de_Valores('5'),text="5", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot14.place(x=87, y=180)

bot15 = Button(frame_corpo, command= lambda: Entrada_de_Valores('6'),text="6", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot15.place(x=170, y=180)

bot16 = Button(frame_corpo, command= lambda: Entrada_de_Valores('-'),text="-", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot16.place(x=250, y=180)

bot17 = Button(frame_corpo, command= lambda: Entrada_de_Valores('1'),text="1", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot17.place(x=0, y=240)

bot18 = Button(frame_corpo, command= lambda: Entrada_de_Valores('2'),text="2", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot18.place(x=87, y=240)

bot19 = Button(frame_corpo, command= lambda: Entrada_de_Valores('3'),text="3", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot19.place(x=170, y=240)

bot20 = Button(frame_corpo, command= lambda: Entrada_de_Valores('+'),text="+", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot20.place(x=250, y=240)

bot21 = Button(frame_corpo, command= lambda: Entrada_de_Valores('±'),text="±", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot21.place(x=0, y=300)

bot22 = Button(frame_corpo, command= lambda: Entrada_de_Valores('0'),text="0", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot22.place(x=87, y=300)

bot23 = Button(frame_corpo, command= lambda: Entrada_de_Valores('.'),text=".", width=10,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot23.place(x=170, y=300)

bot24 = Button(frame_corpo, command= calcular,text="=", width=11,height=3, font=('Ivy 13 bold') , relief=RAISED, overrelief=RIDGE )
bot24.place(x=250, y=300)



area.mainloop()

