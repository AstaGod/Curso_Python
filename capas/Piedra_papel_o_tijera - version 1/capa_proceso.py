import capa_entrada
if capa_entrada.numerjugar==2:
 nombre1=input("Ingresa tu nombre jugador 1: ")
 nombre2=input("Ingresa tu nombre jugador 2: ")
 jugador1=input(f"{nombre1} ingrese entre piedra,papel o tijera: ")
 jugador2=input(f"{nombre2} ingrese entre piedra,papel o tijera: ")
 jugar1andjugar2=jugador1 and jugador2
else:
 print("La cantidad de jugadores debe ser 2 basura humana")