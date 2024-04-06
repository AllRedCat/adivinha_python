from random import randrange

def jogo():
    pontuacao = 10
    valor_certo = randrange(0, 100)
    chute = -1
    while chute != valor_certo:
        chute = int(input("Chute um numero de 0 a 100: "))
        if chute < valor_certo:
            pontuacao -= 1
            print("Chute mais alto")
        elif chute > valor_certo:
            pontuacao -= 1
            print("Chute mais baixo")
    return pontuacao

continuar = "s"
while continuar == "s":
    quantos_pontos_fiz = jogo()
    print(f"Você fez {quantos_pontos_fiz} nessa rodada!")
    continuar = input("Jogar de novo? (s/n) ")