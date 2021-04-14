from random import randint


class Cartas:
    cartas = ["Pedra", "Papel", "Tesoura"]

    def distribuir_cartas(self):

        count = 1
        cartas_a_serem_entregues = []
        while count <= 3:
            count += 1
            numero_da_carta = randint(0, 2)
            cartas_a_serem_entregues.append(self.cartas[numero_da_carta])
        return cartas_a_serem_entregues
