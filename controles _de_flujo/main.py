
##bucles
#condicion=0
#while condicion<11:
    #print(condicion)
    #condicion=condicion+1

#condicion1=0
#while condicion1<21:
    #print(condicion1)
    #condicion1=condicion1+2

#edad=0
#while edad!=20:
    #edad=int(input("Ingrese su edad: "))

#nombre=""
#while nombre!="si":
    #nombre=input("Ingrese su nombre: ")

#while True:
    #nombre1=input("como te llamas: ")
    #if nombre1=="si":
       # break


for numero in range(1,21):
    print(numero)

vocales=["a","e","i","o","u"]
for numero in range(0,5):
    print(vocales[numero])

for vocal in vocales:
    print(vocal)

## CREAR UNA LISTA DE CINCO COLORES CADA COLOR QUE INTERES
## TENDRAS QUE MOSTRAR POR CONSOLA SOLO CUANDO ENCUENTRE EL 
## COLOR ROJO MOSTRARA EL MENSAJE DE
## COLO ENCONTRADO Y SE TERMINARA LA EJECUCION

colores=["negro","azul","rosa","rojo","amarillo"]
for color in colores:
    print(color)
    if color == "rosa":
        print("color encontrado")
        break
    
colores=["negro","azul","rosa","rojo","amarillo"]
for color in colores:
    if color == "rojo":
     print("encontrado")
     break
    print(color)