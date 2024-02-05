import random

def ataque_malicioso(PS_oponente, defensa_oponente):
    defensa_oponente -= 10
    if defensa_oponente <= 0:
        defensa_oponente = 1
    return (PS_oponente, defensa_oponente)

def ataque_placaje(PS_oponente, defensa_oponente):
    PS_oponente -= 35 * (100 / defensa_oponente)
    return (PS_oponente, defensa_oponente)

def ataque_ascuas(PS_oponente, defensa_oponente):
    # Implementa la lógica del ataque "ascuas" si es necesario
    return (PS_oponente, defensa_oponente)

def ataque_oponente(PS_jugador, defensa_jugador):
    ataque = random.randint(1, 3)
    if ataque == 1:
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1
    elif ataque == 2:
        PS_jugador -= 35 * (100 / defensa_jugador)
    elif ataque == 3:
        PS_jugador -= 40
    return (PS_jugador, defensa_jugador)

PS_jugador = 100
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador == "malicioso":
        PS_oponente, defensa_oponente = ataque_malicioso(PS_oponente, defensa_oponente)
    elif ataque_jugador == "placaje":
        PS_oponente, defensa_oponente = ataque_placaje(PS_oponente, defensa_oponente)
    elif ataque_jugador == "ascuas":
        PS_oponente, defensa_oponente = ataque_ascuas(PS_oponente, defensa_oponente)
    else:
        print("¿Qué estás haciendo? ¡Tus ataques son malicioso, placaje y ascuas!")
        continue

    PS_jugador, defensa_jugador = ataque_oponente(PS_jugador, defensa_jugador)

if PS_oponente <= 0 and PS_jugador <= 0:
    print("empate")
elif PS_oponente <= 0:
    print("¡Felicidades, has ganado!")
else:
    print("Lo siento, has perdido")
