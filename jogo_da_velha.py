def exibir_tabuleiro(tabuleiro):
    print("Tabuleiro:")
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")
    print()

def verificar_vitoria(tabuleiro, simbolo):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(simbolo) == 3:
            return True

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == simbolo and tabuleiro[1][coluna] == simbolo and tabuleiro[2][coluna] == simbolo:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        return True

    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:        
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Digite o número da linha (0, 1 ou 2): "))
        coluna = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            jogadas += 1

            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print("Jogador", jogador, "venceu!")
                break

            if jogadas == 9:
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador = "O" if jogador == "X" else "X"
        else:
            print("Posição inválida. Tente novamente.")

jogar_jogo_da_velha()