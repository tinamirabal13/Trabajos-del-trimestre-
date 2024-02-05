import random

jugador = (100, 100)  # Tupla para almacenar los puntos de salud y defensa del jugador
oponente = (100, 100)  # Tupla para almacenar los puntos de salud y defensa del oponente

ataques = {
    "malicioso": (-10, 0),
    "placaje": (0, 0),  # Se calculará antes de aplicarlo
    "ascuas": (0, 0),
}

while jugador[0] > 0 and oponente[0] > 0:
    ataque_jugador = input("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador in ataques:
        efecto = ataques[ataque_jugador]
        if ataque_jugador == "placaje":
            efecto = (-35 * (100 / oponente[1]), 0)
        oponente = (oponente[0] + efecto[0], oponente[1] + efecto[1])
        if oponente[1] <= 0:
            oponente = (oponente[0], 1)
    else:
        print("¿Qué estás haciendo? ¡Tus ataques son malicioso, placaje y ascuas!")
        continue

    # Turno del oponente
    ataque_oponente = random.choice(list(ataques.keys()))
    efecto = ataques[ataque_oponente]
    if ataque_oponente == "placaje":
        efecto = (-35 * (100 / jugador[1]), 0)
    elif ataque_oponente == "latigo":
        efecto = (-10, -10)
    jugador = (jugador[0] + efecto[0], jugador[1] + efecto[1])
    if jugador[1] <= 0:
        jugador = (jugador[0], 1)

# Si termina el ciclo alguien ha ganado
if oponente[0] <= 0 and jugador[0] <= 0:
    print("empate")
elif oponente[0] <= 0:  # ya sabemos que el jugador es >0
    print("felicidades, has ganado")
else:  # ya sabemos que el oponente es >0
    print("Lo siento, has perdido")
