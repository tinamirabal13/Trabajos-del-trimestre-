import random

ataques_jugador = {
    "malicioso": 10,
    "placaje": 35,
    "ascuas": 0
}

ataques_oponente = {
    1: 10,  # latigo
    2: 35,  # placaje
    3: 40   # Pistola de agua
}

PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    
    if ataque_jugador in ataques_jugador:
        if ataque_jugador == "malicioso":
            defensa_oponente -= ataques_jugador[ataque_jugador]
            if defensa_oponente <= 0:
                defensa_oponente = 1
        elif ataque_jugador == "placaje":
            PS_oponente -= ataques_jugador[ataque_jugador] * (100 / defensa_oponente)
        elif ataque_jugador == "ascuas":
            pass
    else:
        print("¡Qué estás haciendo? Tus ataques son malicioso, placaje y ascuas!")
        continue

    ataque_oponente = random.choice(list(ataques_oponente.keys()))
    
    if ataque_oponente == 1:  # latigo
        defensa_jugador -= ataques_oponente[ataque_oponente]
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque_oponente == 2:  # placaje
        PS_jugador -= ataques_oponente[ataque_oponente] * (100 / defensa_jugador)
    elif ataque_oponente == 3:  # Pistola de agua
        PS_jugador -= ataques_oponente[ataque_oponente]

if PS_oponente <= 0 and PS_jugador <= 0:
    print("¡Empate!")
elif PS_oponente <= 0:
    print("¡Felicidades, has ganado!")
else:
    print("Lo siento, has perdido")
