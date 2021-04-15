from Cartas import *


class Jogadores:
    nome_dos_jogadores = []
    cartas_do_jogador = []

    def adicionar_jogador(self):
        for i in range(0, 2):
            nome = input("Digite o nome do "+ str(1 + i) +"° jogador: ")
            self.nome_dos_jogadores.append(nome)
        self.entregar_cartas()

    def entregar_cartas(self):
        for i in range(len(self.nome_dos_jogadores)):
            cartas = Cartas().distribuir_cartas()
            self.cartas_do_jogador.append(cartas)

    def jogar_carta(self):
        cartaExiste = False
        carta = input("Qual o número da carta que o jogador "+ self.nome_dos_jogadores[0] + " deseja jogar: ")
        while cartaExiste == False:
            if int(carta) <= len(self.cartas_do_jogador):
                return carta
            else:
                print("A carta não existe!")
                carta = input("Qual o número da carta que o jogador " + self.nome_dos_jogadores[0] + " deseja jogar: ")


    def retirar_carta(self, jogador, carta):
        count = 0
        for i in self.cartas_do_jogador[jogador]:
            if carta in i:
                del(self.cartas_do_jogador[jogador][count])
                break
            count += 1
