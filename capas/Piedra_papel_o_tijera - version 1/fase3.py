import fase2
match fase2.jugar1andjugar2:
    case jugar1andjugar2 if fase2.jugador1=="piedra" and fase2.jugador2=="tijera":
        print(f"Gana {fase2.nombre1}")
    case jugar1andjugar2 if fase2.jugador1=="papel" and fase2.jugador2=="piedra":
        print(f"Gana {fase2.nombre1}")
    case jugar1andjugar2 if fase2.jugador1=="tijera" and fase2.jugador2=="papel":
        print(f"Gana {fase2.nombre1}")
    case jugar1andjugar2 if fase2.jugador1=="piedra" and fase2.jugador2=="piedra":
        print("Empate")
    case jugar1andjugar2 if fase2.jugador1=="papel" and fase2.jugador2=="papel":
        print("Empate")
    case jugar1andjugar2 if fase2.jugador1=="tijera" and fase2.jugador2=="tijera":
        print("Empate")
    case jugar1andjugar2 if fase2.jugador2=="piedra" and fase2.jugador1=="tijera":
        print(f"Gana {fase2.nombre2}")
    case jugar1andjugar2 if fase2.jugador2=="papel" and fase2.jugador1=="piedra":
        print(f"Gana {fase2.nombre2}")
    case jugar1andjugar2 if fase2.jugador2=="tijera" and fase2.jugador1=="papel":
        print(f"Gana {fase2.nombre2}")