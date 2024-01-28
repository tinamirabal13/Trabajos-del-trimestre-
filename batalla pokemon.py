import random #para Randrange (elegir ataque oponente)

PS_jugador = 100 #PS es puntos de salud 
PS_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while PS_jugador > 0 and PS_oponente > 0:
    ataque_jugador = input("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    if ataque_jugador == "malicioso":
        defensa_oponente = defensa_oponente - 10 
        if defensa_oponente <= 0:
           defensa_oponente = 1 
    elif ataque_jugador == "placaje": 
        PS_oponente -= 35 * (100/ defensa_oponente)
    elif ataque_jugador == "ascuas":
     pass
    else:
        print("Que estas haciendo? Tus ataques son malicioso, placaje y ascuas!")
        continue 

"""turno del Oponente
   El turno del oponente se define con un Random
"""
ataque_oponente = random.randrange(1,3+1)
if ataque_oponente == 1: #latigo
   defensa_jugador -= 10
   if defensa_jugador <= 0:
      defensa_jugador = 1
elif ataque_oponente == 2: #placaje 
     PS_jugador -= 35 * (100/defensa_jugador)
elif ataque_oponente == 3: #Pistola de agua
     PS_jugador -=40
     #randrage esta garantizado a ser 1,2 o 3

#Si termina el ciclo alguien ha ganado
if PS_oponente <= 0 and PS_jugador <= 0:
   print("empate")
elif PS_oponente <= 0: #ya sabemos que el jugador es >0
     print("felicidades, has ganado")
else: #ya sabemos que el oponente es >0
    print ("Lo siento, has perdido")
 



