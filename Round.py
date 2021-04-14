from Jogadores import *
import string

class Round:
    round = 3
    continuar = True
    empate = 0
    ganhador = True

    def iniciar_round(self):
        while True:
            iniciar = input("Digite 1 se deseja iniciar o jogo: ")
            if iniciar == "1":
                Jogadores().adicionar_jogador()
                while self.continuar:
                    if self.empate == self.round:
                        print("Ocorreu um empate ninguém ganhou!")
                        break
                    self.jogadas()
                    if self.ganhador:
                        break
                break

    def jogadas(self):
        cartas_jogadas = []

        for r in range(0, self.round):
            for j in range(len(Jogadores().nome_dos_jogadores)):
                jogar_carta = True
                jogador = Jogadores().nome_dos_jogadores[j]
                while jogar_carta:
                    print("\nQual carta o jogador " + jogador +" Deseja jogar? ")

                    for i in range(len(Jogadores().cartas_do_jogador[j])):
                        print(f"{i} - "+"".join(Jogadores().cartas_do_jogador[j][i]))

                    jogada = input("\nEscolha o numero da Carta: ")

                    if jogada == "" or jogada in string.ascii_letters or int(jogada) > 3:
                        print("\nEssa carta não existe!")
                    elif int(jogada) <= len(Jogadores().cartas_do_jogador[j]):
                        carta_jogada = Jogadores.cartas_do_jogador[j][int(jogada)]
                        cartas_jogadas.append(carta_jogada)
                        Jogadores().retirar_carta(j, carta_jogada)
                        jogar_carta = False
                    else:
                        print("O jogador " +jogador+ " não tem está carta!")
            self.ganhador = self.ganhador_da_mao(cartas_jogadas)

            if self.ganhador:
                break

            cartas_jogadas.clear()


    def ganhador_da_mao(self, jogada):
        carta_do_jogador_1 = jogada[0]
        carta_do_jogador_2 = jogada[1]

        if carta_do_jogador_1 == carta_do_jogador_2:
            self.empate += 1
            print("\nEmpate!")
            return False
        elif carta_do_jogador_1 == "Papel" and carta_do_jogador_2 == "Pedra":
            print("\n\033[092mJogador "+ Jogadores.nome_dos_jogadores[0] +" é o vencedor!")
            return True
        elif carta_do_jogador_1 == "Pedra" and carta_do_jogador_2 == "Tesoura":
            print("\n\033[092mJogador " + Jogadores.nome_dos_jogadores[0] + " é o vencedor!")
            return True
        elif carta_do_jogador_1 == "Tesoura" and carta_do_jogador_2 == "Papel":
            print("\n\033[092mJogador " + Jogadores.nome_dos_jogadores[0] + " é o vencedor!")
            return True
        else:
            print("\n\033[092mJogador " + Jogadores.nome_dos_jogadores[1] + " é o vencedor!")
            return True

r = Round()
r.iniciar_round()