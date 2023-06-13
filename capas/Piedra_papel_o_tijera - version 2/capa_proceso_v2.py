import capa_entrada_v2
if capa_entrada_v2.numerjugar==2:
 nombre1=input("Ingresa tu nombre jugador 1: ")
 nombre2=input("Ingresa tu nombre jugador 2: ")
 jugador1=input(f"{nombre1} ingrese entre piedra,papel o tijera: ")
 jugador2=input(f"{nombre2} ingrese entre piedra,papel o tijera: ")
 jugar1andjugar2=jugador1 and jugador2
 match jugar1andjugar2:
    case jugar1andjugar2 if jugador1=="piedra" and jugador2=="tijera":
        print(f"Gana {nombre1}")
    case jugar1andjugar2 if jugador1=="papel" and jugador2=="piedra":
        print(f"Gana {nombre1}")
    case jugar1andjugar2 if jugador1=="tijera" and jugador2=="papel":
        print(f"Gana {nombre1}")
    case jugar1andjugar2 if jugador1=="piedra" and jugador2=="piedra":
        print("Empate")
    case jugar1andjugar2 if jugador1=="papel" and jugador2=="papel":
        print("Empate")
    case jugar1andjugar2 if jugador1=="tijera" and jugador2=="tijera":
        print("Empate")
    case jugar1andjugar2 if jugador2=="piedra" and jugador1=="tijera":
        print(f"Gana {nombre2}")
    case jugar1andjugar2 if jugador2=="papel" and jugador1=="piedra":
        print(f"Gana {nombre2}")
    case jugar1andjugar2 if jugador2=="tijera" and jugador1=="papel":
        print(f"Gana {nombre2}")
else:
 print("La cantidad de jugadores debe ser 2 basura humana")