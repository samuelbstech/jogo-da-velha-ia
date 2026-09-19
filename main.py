import random

# ------- Exibição do tabuleiro -------

def exibir_tabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

# ------- Validações -------

def validar_jogada(tabuleiro, posicao):
    if posicao < 1 or posicao > 9:
        return False
    return tabuleiro[posicao - 1] == "_"

def verificar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]               # diagonais
    ]
    for combo in combinacoes:
        if all(tabuleiro[i] == jogador for i in combo):
            return True
    return False

def verificar_empate(tabuleiro):
    return "_" not in tabuleiro

# ------- Jogadas -------

def jogada_humano(tabuleiro, jogador):
    while True:
        try:
            posicao = int(input(f"  Jogador {jogador}, escolha uma posição (1-9): "))
            if validar_jogada(tabuleiro, posicao):
                tabuleiro[posicao - 1] = jogador
                break
            else:
                print("  Posição inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("  Digite apenas um número entre 1 e 9.")

def jogada_computador(tabuleiro, jogador):
    oponente = "X" if jogador == "O" else "O"

    # 1. Vitória imediata
    for i in range(9):
        if tabuleiro[i] == "_":
            tabuleiro[i] = jogador
            if verificar_vitoria(tabuleiro, jogador):
                print(f"  Computador ({jogador}) jogou na posição {i + 1}.")
                return
            tabuleiro[i] = "_"

    # 2. Bloqueio
    for i in range(9):
        if tabuleiro[i] == "_":
            tabuleiro[i] = oponente
            if verificar_vitoria(tabuleiro, oponente):
                tabuleiro[i] = jogador
                print(f"  Computador ({jogador}) jogou na posição {i + 1}.")
                return
            tabuleiro[i] = "_"

    # 3. Centro
    if tabuleiro[4] == "_":
        tabuleiro[4] = jogador
        print(f"  Computador ({jogador}) jogou na posição 5.")
        return

    # 4. Canto vazio
    cantos = [i for i in [0, 2, 6, 8] if tabuleiro[i] == "_"]
    if cantos:
        escolha = random.choice(cantos)
        tabuleiro[escolha] = jogador
        print(f"  Computador ({jogador}) jogou na posição {escolha + 1}.")
        return

    # 5. Qualquer posição vazia
    vazias = [i for i in range(9) if tabuleiro[i] == "_"]
    if vazias:
        escolha = random.choice(vazias)
        tabuleiro[escolha] = jogador
        print(f"  Computador ({jogador}) jogou na posição {escolha + 1}.")

# ------- Menu e fluxo principal -------

def menu_principal():
    print("\n=== JOGO DA VELHA ===")
    print("1 - Humano vs. Humano")
    print("2 - Humano vs. Computador")
    while True:
        try:
            opcao = int(input("Escolha o modo: "))
            if opcao in [1, 2]:
                return opcao
            else:
                print("Digite 1 ou 2.")
        except ValueError:
            print("Digite apenas um número.")

def iniciar():
    modo = menu_principal()

    print("\nDica: as posições do tabuleiro seguem a numeração abaixo:")
    exibir_tabuleiro(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    while True:
        tabuleiro = ["_"] * 9
        jogadores = ["X", "O"]
        turno = 0

        while True:
            jogador_atual = jogadores[turno % 2]

            exibir_tabuleiro(tabuleiro)

            # Decide quem joga
            if modo == 2 and jogador_atual == "O":
                print(f"  Vez do Computador ({jogador_atual})...")
                jogada_computador(tabuleiro, jogador_atual)
            else:
                jogada_humano(tabuleiro, jogador_atual)

            # Verifica resultado
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                if modo == 2 and jogador_atual == "O":
                    print("  O Computador venceu! Melhor sorte na próxima.")
                else:
                    print(f"  Parabéns! Jogador {jogador_atual} venceu!")
                break

            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("  Empate! Foi quase...")
                break

            turno += 1

        novamente = input("\nJogar novamente? (s/n): ").strip().lower()
        if novamente != "s":
            print("Obrigado por jogar! Até a próxima.")
            break

# Ponto de entrada
iniciar()
