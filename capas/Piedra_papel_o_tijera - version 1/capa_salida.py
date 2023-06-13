import capa_proceso
match capa_proceso.jugar1andjugar2:
    case jugar1andjugar2 if capa_proceso.jugador1=="piedra" and capa_proceso.jugador2=="tijera":
        print(f"Gana {capa_proceso.nombre1}")
    case jugar1andjugar2 if capa_proceso.jugador1=="papel" and capa_proceso.jugador2=="piedra":
        print(f"Gana {capa_proceso.nombre1}")
    case jugar1andjugar2 if capa_proceso.jugador1=="tijera" and capa_proceso.jugador2=="papel":
        print(f"Gana {capa_proceso.nombre1}")
    case jugar1andjugar2 if capa_proceso.jugador1=="piedra" and capa_proceso.jugador2=="piedra":
        print("Empate")
    case jugar1andjugar2 if capa_proceso.jugador1=="papel" and capa_proceso.jugador2=="papel":
        print("Empate")
    case jugar1andjugar2 if capa_proceso.jugador1=="tijera" and capa_proceso.jugador2=="tijera":
        print("Empate")
    case jugar1andjugar2 if capa_proceso.jugador2=="piedra" and capa_proceso.jugador1=="tijera":
        print(f"Gana {capa_proceso.nombre2}")
    case jugar1andjugar2 if capa_proceso.jugador2=="papel" and capa_proceso.jugador1=="piedra":
        print(f"Gana {capa_proceso.nombre2}")
    case jugar1andjugar2 if capa_proceso.jugador2=="tijera" and capa_proceso.jugador1=="papel":
        print(f"Gana {capa_proceso.nombre2}")